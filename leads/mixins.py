from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class OrganiserAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is organiser."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organiser:
            return redirect('/leads')
        return super().dispatch(request, *args, **kwargs)



