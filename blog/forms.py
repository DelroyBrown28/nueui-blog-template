from django import forms
from .models import Comment, Category
from mptt.forms import TreeNodeChoiceField



class NewCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['parent'].widget.attrs.update(
            {'class' : 'd-none'}
        )
        self.fields['parent'].label = ''
        self.fields['parent'].required = False
    
    class Meta:
        model = Comment
        fields = ('post', 'parent', 'content')
        widgets = {
            'content' : forms.TextInput(attrs={'class' : 'form-control'}),
        }


class PostSearchForm(forms.Form):
    q = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['q'].label = 'Search Form'
        self.fields['q'].widget.attrs.update(
            {'class': 'form-control menudd', 'placeholder' : 'Search'})
    
