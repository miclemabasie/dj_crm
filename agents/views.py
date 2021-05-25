import random

from django.shortcuts import render, reverse
from django.views import generic
from leads.models import Agent
from .forms import AgentCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import OrganiserAndLoginRequiredMixin
from django.core.mail import send_mail


class AgentListView(OrganiserAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/agent-list.html'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentCreateView(OrganiserAndLoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agent-create.html'
    form_class = AgentCreateForm

    def get_success_url(self):
        return reverse('agents:agent_list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent=True
        user.is_organiser = False
        user.set_password(f"{random.randint(0, 1000000)}")
        user.save()
        send_mail(subject='You were made an agent', 
            message='You have an agent account in DJ-CRM, please follow the link attatched to this email to login and get started, We hope to see you..',
            from_email='us@django.com',
            recipient_list=(user.email,))
        
        Agent.objects.create(
            user=user,
            organisation=self.request.user.userprofile
        )
       
        return super(AgentCreateView, self).form_valid(form)
    

    
class AgentDetailView(OrganiserAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/agent-detail.html'
    context_object_name = 'agent'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

class AgentUpdateView(OrganiserAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agent-update.html'
    form_class = AgentCreateForm

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    def get_success_url(self):
        return reverse('agents:agent_list')


class AgentDeleteView(OrganiserAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/agent-delete.html'
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    
    def get_success_url(self):
        return reverse('agents:agent_list')
