from django import forms


class ItemForm(forms.Form):
    fulltext = forms.CharField(label='Volltext *', max_length=100)
