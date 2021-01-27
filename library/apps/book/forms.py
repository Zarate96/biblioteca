from django import Forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model =  Author
        fields = ['name','last_name', 'nationality', 'description']
