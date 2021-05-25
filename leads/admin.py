from django.contrib import admin
from .models import Lead, Agent, User, UserProfile, Category



admin.site.register(Agent)
admin.site.register(User)
admin.site.register(Category)

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'agent']

admin.site.register(UserProfile)