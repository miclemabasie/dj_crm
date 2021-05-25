from django.urls import path
from .views import (
    LeadListView,
    LeadDetailView,
    LeadCreateView,
    LeadUpdateView,
    LeadDeleteView,
    AssignAgentView,
    CategoryListView,
    CategoryDetailView,
    CategoryUpdateView,
  

) 
app_name = 'leads'

urlpatterns = [


    path('', LeadListView.as_view(), name='lead_list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
    path('update/<int:pk>/', LeadUpdateView.as_view(), name='lead_update'),
    path('delete/<int:pk>/', LeadDeleteView.as_view(), name='lead_delete'),
    path('assign-lead/<int:pk>/', AssignAgentView.as_view(), name='assign-lead'),
    path('create/', LeadCreateView.as_view(), name='create_lead'),
    path('category-list/', CategoryListView.as_view(), name='category-list'),
    path('<int:pk>/category-detail/', CategoryDetailView.as_view(), name='category-detail'),
    path('<int:pk>/category-update/', CategoryUpdateView.as_view(), name='category-update'),

]
