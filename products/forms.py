from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """ 
    a simple comment form that only asks the user to input their text
    other comment information will be pulled from elsewhere
    """
    class Meta:
        model = Comment
        fields = ['body']