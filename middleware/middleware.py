from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import redirect
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
class LoginRequiredMiddleware:
    """
    Middleware to check if user is authenticated before allowing access to views.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.jwt_authenticator = JWTAuthentication()

    def __call__(self, request):
        # Check if the request path requires login (exclude paths that don't need authentication)
        login_exempt_paths = [
            reverse('api-login'),
            reverse('api-signup'),  # Assuming 'api-login' is a valid URL name
            reverse('token_obtain_pair'),  # Add the token endpoint to the exempt paths
            reverse('token_refresh')  # If you have a token refresh endpoint
        ]
        if request.path_info.startswith('/api/') and request.path_info not in login_exempt_paths:
            print(request.path_info)
            try:
                user, token = self.jwt_authenticator.authenticate(request)
                print(user, token)
                if user:
                    request.user = user
                print(user.is_authenticated)
            except (InvalidToken, TokenError) as e:
                pass
            if not request.user.is_authenticated:
                print("GOT IN NOT TRUE")
                if request.method == 'GET':  # Redirect only GET requests
                    print("GOING TO API-LOGIN")
                    return redirect(reverse('api-login'))  # Redirect to login endpoint
                elif request.method == 'POST':  # For POST requests, return a 403 JSON response
                    return JsonResponse({'error': 'Authentication required'}, status=403)

        response = self.get_response(request)
        return response
