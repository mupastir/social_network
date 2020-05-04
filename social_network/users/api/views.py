from rest_auth.registration.views import RegisterView

from .serializers import UserRegisterSerializer


class UserRegisterView(RegisterView):
    serializer_class = UserRegisterSerializer
    permission_classes = ()
    authentication_classes = ()
