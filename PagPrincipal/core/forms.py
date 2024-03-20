from django import forms
from .models import Cliente

class ClienteLoginForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

class ClienteRegistroForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Cliente
        fields = ['nombreCliente', 'telefono', 'direccion', 'email', 'region', 'comuna']

    def clean_password2(self):
        # Verifica que las contraseñas coincidan
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

    def save(self, commit=True):
        # Guarda el usuario y su contraseña de manera segura
        user = super().save(commit=False)
        password = self.cleaned_data["password1"]
        if password:
            # Aquí usamos el gestor personalizado para crear el usuario con contraseña segura
            user.set_password(password)
        if commit:
            user.save()
        return user