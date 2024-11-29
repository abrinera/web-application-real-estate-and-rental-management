from django import forms
from .models import Employee, Client

# to add form input for employee signin_signup
class EmployeeForm(forms.ModelForm):
    class Meta:
        model =  Employee
        fields =  ['username', 'gender','email', 'employee_id' ,'password']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone', 'age', 'nid', 'address', 'gender', 'job', 'date_of_birth', 'property_id']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Enter date of birth'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Enter last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Enter email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Enter phone'}),
            'age': forms.NumberInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Enter age'}),
            'nid': forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Enter NID'}),
            'address': forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Enter address'}),
            'gender': forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Enter Gender'}),
            'job': forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Enter job'}),
            'property_id': forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Enter property ID'}),
        }

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = False