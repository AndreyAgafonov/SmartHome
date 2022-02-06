from django import forms
from django.core.exceptions import ValidationError
from smarthome.models import SettingsAgentsConfig,Settings
# from users.models import User
#
# class UserLoginForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ('username','password')

class settingsAgentAddForm(forms.ModelForm):
    class Meta:
        model = SettingsAgentsConfig
        fields = ['name', 'address', 'sshUser', 'sshPrivateKey', 'description']


class settingsAgentAddForm1(forms.Form):
    name = forms.CharField(max_length=64, label='Client name')
    address = forms.CharField(max_length=50, label='Client address')
    sshUser = forms.CharField(max_length=64, label='Client ssh user name')
    sshPrivateKey = forms.CharField(max_length=4120, label='Client ssh private key(RSA)')
    description = forms.CharField(max_length=4120, label='description', required=False)


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['settingsValueBoolean']
        widgets = {
            'settingsValueBoolean': forms.CheckboxInput(attrs={'title': 'test help'})
        }

