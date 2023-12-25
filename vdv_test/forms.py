from django import forms


class ProjectForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    countUsers = forms.IntegerField()

# Textarea() многострочное поле ввода текста

class ProjectFilterForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    countUsers = forms.IntegerField(required=False)


class ProjectUpdateForm(forms.Form):
    title = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)
