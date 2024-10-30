from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, f"{i} estrellas") for i in range(1, 6)]),
        }
