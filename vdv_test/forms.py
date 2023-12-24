from django import forms


class ProjectForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    countUsers = forms.IntegerField()

# Textarea() многострочное поле ввода текста