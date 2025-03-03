from django.http import JsonResponse

API_KEY = "my_secret_api_key"  # Change this to a secure key

class APIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/graphql/"):  # Protect GraphQL endpoint
            api_key = request.headers.get("X-API-KEY")
            if api_key != API_KEY:
                return JsonResponse({"error": "Unauthorized"}, status=403)
        return self.get_response(request)
