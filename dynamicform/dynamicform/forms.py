from django import forms


class UserForm(forms.Form):
    input_name0 = forms.CharField(label='input_name0', max_length=40, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Input_name0',
        }
    ))
