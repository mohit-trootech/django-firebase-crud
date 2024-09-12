from django import forms
from firebase.utils.constants import Employees


class Employee(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": True}),
        label="Name",
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control", "required": True}),
        label="Age",
    )
    position = forms.ChoiceField(
        choices=Employees.POSITION_CHOICES.value,
        widget=forms.Select(attrs={"class": "form-control", "required": True}),
        label="Position",
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": True}),
        label="City",
    )
    salary = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"class": "form-control", "required": True, "step": "0.01"}
        ),
        label="Salary",
    )
    joined = forms.DateField(
        widget=forms.DateInput(
            attrs={"class": "form-control", "required": True, "type": "date"}
        ),
        label="Joined",
    )
    status = forms.ChoiceField(
        choices=Employees.STATUS_CHOICES.value,
        widget=forms.Select(attrs={"class": "form-control", "required": True}),
        label="Status",
    )

    def clean_salary(self):
        salary = self.cleaned_data.get("salary")
        if salary is not None and salary <= 0:
            raise forms.ValidationError("Salary must be a positive number.")
        return salary
