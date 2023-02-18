from .views import *
from .models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm




class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password3': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'size': '35px'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class ChangeProfile(ModelForm):
    bio = forms.CharField(label='Біографія', widget=forms.Textarea(attrs={'class': 'form-input'}))
    class Meta:
        model = Profile
        fields = ('bio',)



# class RegisterUsersForm(forms.ModelForm):
#     confirm_password = forms.CharField(label='Confirm', widget=forms.PasswordInput())

#     class Meta:
#         model = Register
#         fields = ['username', 'password', 'confirm_password']
#         widgets = {
#             'username': forms.TextInput({'class': 'form-input'})
#         }

#     def clean_confirm_password(self):
#         password = self.cleaned_data['password']
#         confirm_password = self.cleaned_data['confirm_password']
        
#         if password != confirm_password:
#             raise forms.ValidationError('Паролі не співпадають!')

#         return self.cleaned_data['username']


            

        

    

    # class Meta:
    #     model = Register
    #     fields = ['username', 'password', 'confirm_password']
    #     widgets = {
    #         'username': forms.TextInput(attrs={'size': 30})
    #     }

    # def clean_username(self):
    #     username = self.cleaned_data['username']

    #     if len(username) > 64:
    #         raise forms.ValidationError('Нікнейм повинен бути менше за 64 символів')

    #     return username

    # def clean_password(self):
        
    #     print(self.confirm_password)
        # confirm_password = self.cleaned_data['confirm_password']

        # if password != confirm_password:
        #     raise forms.ValidationError('Error!')
