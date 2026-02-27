from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


@extend_schema_view(
    post=extend_schema(
        summary="Create user",
        description="Creates a new user. Available for everybody.",
        tags=["Users"],
        responses={201: UserSerializer},
    )
)
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)  # позволяет неавторизованным пользователям зарегистрироваться
