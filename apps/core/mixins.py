from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.views import redirect_to_login
from django.contrib import messages
from django.shortcuts import redirect
from django.core.exceptions import ImproperlyConfigured

class AnonymousMixin(AccessMixin):

    def handle_no_permission(self):
        # message = messages.success(request, '{ "message" : "شما دسترسی به این صفحه ندارید " }')
        return redirect("pages:index")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class SignInRequiredMixin(AccessMixin):

    next_url = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("pages:singin" + f"?next=next_url")
        return super().dispatch(request, *args, **kwargs)



class ProducerOnlyMixin(AccessMixin):
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_producer:
            messages.error(request, '{ "message": "you don\'t have permissions!" }')
            return redirect("userpanel:index")
        return super().dispatch(request, *args, **kwargs)


class AdminOnlyMixin(AccessMixin):

    def handle_no_permission(self):
        messages.success(self.request, '{ "message" : "شما به این صفحه دسترسی ندارید " }')
        return redirect('users:userpanel')
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff or not request.user.is_superuser:
            return self.handle_no_permission
        return super().dispatch(request, *args, **kwargs)