from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user_name', 'name_of_organization', 'tin',
                  'phone_number', 'email', 'comment']

        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': "form-control", 'placeholder': "Как к Вам можно обращаться?"}),
            'name_of_organization': forms.TextInput(attrs={
                'class': "form-control", 'placeholder': "Название Вашей организации"}),
            'tin': forms.TextInput(attrs={
                'class': "form-control", 'placeholder': "ИНН"}),
            'phone_number': forms.TextInput(attrs={
                'class': "form-control", 'placeholder': "Ваш номер телефона"}),
            'email': forms.EmailInput(attrs={
                'class': "form-control", 'placeholder': "Ваш адрес электронной почты"}),
            'comment': forms.Textarea(attrs={
                'class': "form-control", 'placeholder': "Дополнительная информация о заказе"})
        }



