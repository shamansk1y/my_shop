from main_page.models import Subscription, ContactUs, Review
from django import forms


class SubscriptionForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'type': "text",
                'class': "form-control",
                'placeholder': "Ваш Email",
            }))
    class Meta:
        model = Subscription
        fields = ['email']


class ContactUsForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control",
                'id': "name",
                'placeholder': "Ваше ім'я",
                'required': "required",
                'data-validation-required-message': "Please enter your name",
            }))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'type': "email",
                'class': "form-control",
                'id': "email",
                'placeholder': "Ваш Email",
                'required': "required",
                'data-validation-required-message': "Please enter your email",
            }))

    subject = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control",
                'id': "subject",
                'placeholder': "Тема повідомлення",
                'required': "required",
                'data-validation-required-message': "Please enter a subject",
            }))


    message = forms.CharField(
        max_length=300,
        widget=forms.Textarea(
            attrs={
                'class': "form-control",
                'rows': "8",
                'id': "message",
                'placeholder': "Текст повідомлення",
                'required': "required",
                'data-validation-required-message': "Please enter your message",
            }))

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'name', 'email', 'message']

    name = forms.CharField(label="Ім'я", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ваше ім'я"}))
    email = forms.EmailField(label='Еmail', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш email'}))
    message = forms.CharField(label='Коментар', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Ваш відгук'}))
    rating = forms.ChoiceField(choices=[(1, ''), (2, ''), (3, ''), (4, ''), (5, '5')], widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}), label='Оцінка в 1 до 5')

