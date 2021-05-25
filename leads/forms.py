from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from django import forms
from .models import Lead, Agent

User = get_user_model()

class LeadCreateForm(forms.ModelForm):
    
    class Meta:
        model = Lead
        fields = (
        "first_name",
        "last_name",
        "age", 
        "agent",
        "category",
        "description",
    
        "phone_number",
        "email",
)


class CreateLeadForm(forms.Form):
    first_name = forms.CharField(max_length=300)
    last_name = forms.CharField(max_length=300)
    age = forms.IntegerField(min_value=20)



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
        

class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        agents = Agent.objects.filter(organisation=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields['agent'].queryset = agents


class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['category']