#-*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Counter
from forms import SetPassForm
import genpassword, os, random

def gen_passwords(dictionary_file, num=10, lenth=10, numbers=False, upper=False):
    """return list passwords
    Arguments:
    - `dictionary`: rules
    """
    main_dict = genpassword.get_dict_from_file(dictionary_file)
    list_password = [ genpassword.gen_password_with_none(main_dict, lenth) for i in range(num) ]
    count = 0
    for password in list_password:
        if numbers:
            if random.choice([True, False]):
                password = password.replace('ch', '4')
                if random.choice([True, False]):
                    password = password.replace('o', '0')
        if upper:
            symbol_list = list(password)
            for i in range(len(symbol_list)):
                if random.choice([True, False]):
                    symbol_list[i] = symbol_list[i].upper()
            password = ''
            for i in symbol_list:
                password = password + i
        list_password[count] = password
        count += 1
    return list_password

def main_page(request):
    """главная вьюха
    Arguments:
    - `request`:
    """
    if request.method == 'POST':
        radioform = SetPassForm(request.POST)
        radioform.is_valid()
        num_passwords = int(radioform.cleaned_data['num_pass'])
        passwords = gen_passwords(os.path.dirname(__file__) + '/dicts/' + radioform.cleaned_data['language'],
                                  num=num_passwords,
                                  lenth=int(radioform.cleaned_data['lenth_pass']),
                                  upper=radioform.cleaned_data['upper_pass'],
                                  numbers=radioform.cleaned_data['string_replace_num'])
    else:
        passwords = gen_passwords(os.path.dirname(__file__) + '/dicts/italian')
        num_passwords = 10
        radioform = SetPassForm({'num_pass':'10', 'lenth_pass':'10', 'language':'italian'})
    count = Counter()
    counter = count.get_counter(num_passwords)
    return render_to_response('index.html', {
            'counter':counter,
            'passwords':passwords,
            'radioform':radioform,
            'browser':request.META['HTTP_USER_AGENT'],
            'ip':request.META['REMOTE_ADDR']
            }, context_instance = RequestContext(request))
