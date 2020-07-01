from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny



from account.models import Account
from .serializers import RegistrationSerializer, AccountPropertiesSerializer, UserLoginSerializer


def validate_username(username):
    try:
        account = Account.objects.get(username=username)
    except Account.DoesNotExist:
        return None
    if account != None:
        return username


@api_view(['POST', ])
@permission_classes((AllowAny,))
def registration_view(request):
    if request.method == 'POST':
        data = {}
        username = request.headers['username']
        if validate_username(username) != None:
            data['error_message'] = 'That username is already in use.'
            data['response'] = 'Error'
            return Response(data)
        data = {'username' : username, 'password': request.headers['password']}
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['pk'] = account.pk
            # token = Token.objects.get(user=account).key
            # data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


@api_view(['GET', ])
@permission_classes((AllowAny,))
def all(request):
    posts = Account.objects.all()
    serializer = AccountPropertiesSerializer(posts, many=True)
    return Response(serializer.data)






class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):

        data = {'username': request.headers['username'],
                                                 'password': request.headers['password']}
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)