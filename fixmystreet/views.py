from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def root_url(request):
    return Response(
        {
            "message": "API is running",
            "endpoints": {
                "register": "/api/users/",
                "login": "auth/jwt/create",
                "profile": "auth/users/me",
                "problem": "api/problem/",
                "problem detail": "api/problem/<id>",
            },
        }
    )
