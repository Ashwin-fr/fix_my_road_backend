from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

class EmailBackend(BaseBackend):

    def authenticate(self, request, username = None, password = None, **kwargs):
    
        try:

            user_object = User.objects.get(email= username)

            if user_object.check_password(password):

                return user_object
            
            else:

                return None
            

        except:

            return None
        
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        