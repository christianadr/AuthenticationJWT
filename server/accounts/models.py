from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):

    """ 
    Creates and returns a new user for authentication

    Parameters:
        - email (str)
        - name (str)
        - password (str, optional)

    Returns: 
        - user
    """
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('User must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password) # converts plain text password into its hash version
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    
    
    def get_short_name(self):
        return self.name
    

    # expects to return email in string
    def __str__(self) -> str:
        return self.email
