from django import forms

class NumberForm(forms.Form):
    a = forms.IntegerField(label="Number A")
    b = forms.IntegerField(label="Number B")
    c = forms.IntegerField(label="Number C")
    d = forms.IntegerField(label="Number D")
    e = forms.IntegerField(label="Number E")
    