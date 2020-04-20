from django import forms


class Form(forms.Form):
  message = forms.CharField(max_length=151)

