#-*- coding: utf-8 -*-

from django import forms

NUM_VARIANTS = [(i+1, i+1) for i in range(20)]
LENTH_PASS = [(i+1, i+1) for i in range(20)]
LANG = [('italian', 'Итальянский'), ('french','Французский'), ('japanese', 'Японский')]

class SetPassForm(forms.Form):
    language = forms.ChoiceField(label='Язык пароля', widget=forms.Select, choices=LANG)
    num_pass = forms.ChoiceField(label='Количество паролей', widget=forms.Select, choices=NUM_VARIANTS)
    lenth_pass = forms.ChoiceField(label='Длина пароля', widget=forms.Select, choices=LENTH_PASS)
    upper_pass = forms.BooleanField(label='Прописные буквы', required=False)
    string_replace_num = forms.BooleanField(label='Использовать цифры', required=False)

