from django.shortcuts import render, redirect, reverse
from .models import User, Lead, Agent, Category
from django.http import Http404, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LeadCreateForm, CreateLeadForm, LeadCategoryUpdateForm
from .forms import CustomUserCreationForm, AssignAgentForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, View, FormView
# from django.contrib.auth.views import 
from .mixins import OrganiserAndLoginRequiredMixin


def home_page(request):
    template_name = "pages/home.html"
    context = {
        'title': "Home Page",
    }

    return render(request, template_name, context)
    

class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    
class LeadListView(LoginRequiredMixin, ListView):
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user
        # filter the for the entire Organisation
        if user.is_organiser:
            queryset = Lead.objects.filter(organisation=user.userprofile, agent__isnull=False)
        else:
            # filter for logged in user
            queryset = Lead.objects.filter(organisation=user.agent.organisation, agent__isnull=False)
            queryset = queryset.filter(agent__user=user)
        
        return queryset

    def get_context_data(self, *args, **kwargs):
        user = self.request.user
        context = super(LeadListView, self).get_context_data(**kwargs)
        if user.is_organiser is False:
            context.update({
                'organisation': user.agent.organisation
            })
        if user.is_organiser:
            queryset = Lead.objects.filter(organisation=user.userprofile, agent__isnull=True)


            context.update({
                'unassigned_leads': queryset,
                
            })

        return context


class LeadDetailView(LoginRequiredMixin, DetailView):

    template_name = 'leads/lead_detail.html'
    context_object_name = 'lead'
    
    def get_queryset(self):
        user = self.request.user
    # filter the for the entire Organisation
        if user.is_organiser:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            # filter for logged in user
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            queryset = queryset.filter(agent__user=user)
        
        return queryset
    

    

class LeadCreateView(OrganiserAndLoginRequiredMixin, CreateView):
    form_class = LeadCreateForm
    template_name = 'leads/lead_create.html'



    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.organisation = self.request.user.userprofile
        print(lead.first_name, lead.organisation)
        lead.save()
        return super(LeadCreateView, self).form_valid(form)
    def get_success_url(self):
        return reverse("leads:lead_list")     


class LeadUpdateView(OrganiserAndLoginRequiredMixin, UpdateView):
    template_name = 'leads/leads_update.html'
    form_class = LeadCreateForm
    
    def get_queryset(self):
        user = self.request.user
    # filter the for the entire Organisation
        if user.is_organiser:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        return queryset

    def get_success_url(self):
        return reverse('leads:lead_list')

   
class LeadDeleteView(OrganiserAndLoginRequiredMixin, DeleteView):
    template_name = 'leads/lead_delete.html'

    def get_queryset(self):
        user = self.request.user
    # filter the for the entire Organisation
        if user.is_organiser:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        return queryset 

    def get_success_url(self):
        return reverse('leads:lead_list')

class AssignAgentView(OrganiserAndLoginRequiredMixin, FormView):
    template_name = 'leads/assign-agent.html'
    form_class = AssignAgentForm

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs(*args, **kwargs)
        kwargs.update({
            'request': self.request
        })

        return kwargs

    def get_success_url(self):
        return reverse('leads:lead_list')

    def form_valid(self, form):
        print(form.cleaned_data.get('agent'))
        agent = form.cleaned_data.get('agent')
        lead = Lead.objects.get(id=self.kwargs['pk'])
        lead.agent=agent
        lead.save()
        return super(AssignAgentView, self).form_valid(form)


class CategoryListView(LoginRequiredMixin, ListView):
    template_name = 'leads/category-list.html'

    context_object_name = 'categories'

    def get_queryset(self):
        user = self.request.user
        # Getting the initail queryset 
        if user.is_organiser:
            queryset = Category.objects.filter(organisation=user.userprofile)
        else:
            queryset = Category.objects.filter(organisation=user.agent.organisation)

        return queryset 

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(CategoryListView, self).get_context_data(**kwargs)

        if user.is_organiser:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
        
        context.update({
            'unassigned_lead_count': queryset.filter(category__isnull=True).count()
        })
        return context
    

class CategoryDetailView(LoginRequiredMixin, DetailView):

    template_name = 'leads/category-detail.html'
    context_object_name = 'category'

    def get_queryset(self):
        user = self.request.user
        # Getting the initail queryset 
        if user.is_organiser:
            queryset = Category.objects.filter(organisation=user.userprofile)
        else:
            queryset = Category.objects.filter(organisation=user.agent.organisation)

        return queryset 

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        leads = self.get_object().leads.all()
        context.update({
            'leads': leads
        })
        print(leads)
        return context


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'leads/category-update.html'
    form_class = LeadCategoryUpdateForm


    def get_queryset(self):
        user = self.request.user

        # Getting the initail queryset for the entire organisation
        if user.is_organiser:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            # Filter for the agent that is logged in
            queryset = queryset.filter(agent__user=user)
        
        return queryset
    
    def get_success_url(self):
        return reverse('leads:lead_detail', kwargs={'pk': self.get_object().id})