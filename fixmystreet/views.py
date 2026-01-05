from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def root_url(request):
    return Response(
        {
            "message": "API is running",
            "endpoints": {
                "register": "/api/register/",
                "login": "auth/jwt/create",
                "user": "api/user",
                "profile": "auth/users/me",
                "problem": "api/problem/",
                "problem detail": "api/problem/id",
            },
        }
    )
