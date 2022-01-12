from django import forms

class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())

   def clean_message(self):
     username = self.cleaned_data.get("username")
     print('clean', username)
     return username


class ApplyForm(forms.Form):
   longitude = forms.CharField(max_length = 100)
   latitude = forms.CharField(max_length = 100)
   username = forms.CharField(max_length = 100)

   def clean_message(self):
     longitude = self.cleaned_data.get("longitude")
     latitude = self.cleaned_data.get("latitude")
     username = self.cleaned_data.get("username")
     print('clean', longitude)
     return latitude
