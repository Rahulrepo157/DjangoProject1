from django import forms
from .models import DemoRequest

class DemoRequestForm(forms.ModelForm):
    class Meta:
        model = DemoRequest
        fields = ['name', 'company_name', 'email', 'phone_number', 'message']
        # You can add widgets here later if needed, for example:
        # widgets = {
        #     'message': forms.Textarea(attrs={'rows': 4}),
        # }
