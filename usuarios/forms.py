from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.UserRegister
        fields = ('first_name', 'last_name', 'gender', 'birth_date', 'cpf',
                  'address', 'city', 'state', 'zip_code', 'email', 'phone',
                  'password','confirm_password',
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Matthew'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mercer'}),
            'gender': forms.Select(attrs={'class':'custom-select'}),
            'birth_date': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'cpf': forms.TextInput(attrs={'type':'text','readonly':'true', 'class':'form-control',
                                          'onfocus':'this.removeAttribute("readonly")', "placeholder":"55566677700"}),
            'address': forms.TextInput(attrs={"class":"form-control", 'placeholder':'Rua Força Pública, 89'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'custom-select'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control', "minlength":"8", "maxlength":"8", 'placeholder':'00000-000'}),
            'password': forms.PasswordInput(attrs={'class':'form-control',}),
            'confirm_password': forms.PasswordInput(attrs={'class':'form-control',}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={
                'class':'form-control',
                'data-inputmask':"'mask': '99999-9999'",
                'data-mask':''})
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 3:
            raise ValidationError("Primeiro nome precisa ter ao menos 3 caracteres.")
        return first_name
        

    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            msg = ValidationError(
                    'Senhas não são iguais', code='password_mismatch'
                )
            self.add_error('password',msg)
            self.add_error('confirm_password',msg)

            return super().clean()

        return super().clean()
        

class RegisterFormServer(forms.ModelForm):
    class Meta:
        model = models.ServerRegister
        fields = ('first_name', 'last_name', 'gender', 'birth_date', 'cpf',
                  'address', 'city', 'state', 'zip_code', 'email', 'phone',
                  'password','confirm_password', 'document', 'service'
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Matthew'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mercer'}),
            'gender': forms.Select(attrs={'class':'custom-select'}),
            'birth_date': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'cpf': forms.TextInput(attrs={'type':'text','readonly':'true', 'class':'form-control',
                                          'onfocus':'this.removeAttribute("readonly")', "placeholder":"55566677700"}),
            'address': forms.TextInput(attrs={"class":"form-control", 'placeholder':'Rua Força Pública, 89'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'custom-select'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control', "minlength":"8", "maxlength":"8", 'placeholder':'00000-000'}),
            'password': forms.PasswordInput(attrs={'class':'form-control',}),
            'confirm_password': forms.PasswordInput(attrs={'class':'form-control',}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={
                'class':'form-control',
                'data-inputmask':"'mask': '99999-9999'",
                'data-mask':''}),
            'document': forms.TextInput(attrs={'class':'form-control'}),
            'service': forms.TextInput(attrs={'class':'form-control'}),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 3:
            raise ValidationError("Primeiro nome precisa ter ao menos 3 caracteres.")
        return first_name
        

    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            msg = ValidationError(
                    'Senhas não são iguais', code='password_mismatch'
                )
            self.add_error('password',msg)
            self.add_error('confirm_password',msg)

            return super().clean()

        return super().clean()