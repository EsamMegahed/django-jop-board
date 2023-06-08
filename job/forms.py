from django import forms
from .models import Apply, Job


class Applyform(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ["name", "email", "website", "cv", "cover_letter"]


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
        exclude = ("slug", "owner")
