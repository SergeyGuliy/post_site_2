# -*- coding: utf-8 -
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User


class OrderForm(forms.Form):

    name = forms.CharField()
    last_name = forms.CharField(required=False)
    phone = forms.CharField()
    buying_type = forms.ChoiceField(widget=forms.Select(), choices=([("self", "Самовывоз"), ("delivery", "Доставка")]))
    date = forms.DateField(widget=forms.SelectDateWidget(), initial=timezone.now())
    address = forms.CharField(required=False)
    comments = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Имя"
        self.fields['last_name'].label = "Фамилия"
        self.fields['phone'].label = "Контактый телефон"
        self.fields['phone'].help_text = "Укажите котактный номер телефона."
        self.fields['buying_type'].label = "Способ получения"
        self.fields['address'].label = "Адресс доставки"
        self.fields['address'].help_text = "Пожалуста, укажите точный адрес доставки"
        self.fields['comments'].label = "Коментарий к заказу"
        self.fields['date'].label = "Дата доставки"
        self.fields['date'].help_text = "Доставка производится на следующий день после оформления заказ"


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_check = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password_check']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Введите ваш LogIn"
        self.fields['username'].help_text = ""
        self.fields['email'].label = "Введите ваш e-mail"
        self.fields['first_name'].label = "Введите ваше имя"
        self.fields['last_name'].label = "Укажите вашу фамилия"
        self.fields['password'].label = "Введите пароль"
        self.fields['password_check'].label = "Повторите пароль"

    def clean(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Данный LogIn занят другим польвателем.')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Данный e-mail занят другим польвателем.')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Введите ваш LogIn."
        self.fields['password'].label = "Введите пароль."

    def clean(self):
        username = self.cleaned_data['username']
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким LogIn не зарегестрирован.')