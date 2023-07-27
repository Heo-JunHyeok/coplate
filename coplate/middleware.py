from django.urls import reverse
from django.shortcuts import redirect


class ProfileSetupMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    # request processing
    def __call__(self, request):
        if (
            request.user.is_authenticated
            and not request.user.nickname
            and request.path_info != reverse("profile-set")
        ):
            return redirect("profie-set")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
