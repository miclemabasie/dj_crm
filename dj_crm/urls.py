from django.contrib.auth.views import (LoginView, 
LogoutView, 
PasswordResetView,
PasswordResetDoneView,
PasswordResetCompleteView,
PasswordResetConfirmView,
)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from leads.views import SignupView, home_page



urlpatterns = [
    path('', home_page, name='home'),
    path('leads/', include('leads.urls', namespace='leads')),
    path('agents/', include('agents.urls', namespace='agents')),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset-password', PasswordResetView.as_view(), name='reset-password'),
    path('password-reset-done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-complete', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('signup/', SignupView.as_view(), name='signup')
]


if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    