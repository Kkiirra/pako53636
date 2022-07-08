from django.shortcuts import render, redirect
from .models import UserModel
from .forms import UserForm
import json


def create_formdata(request):
    """
    Функция при принятии POST запроса проверяет его валидность -
    В случае успеха POST запрос разбивается на кортежи и в цикле создаются объекты класса UserModel
    """
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            for input_name, input_value in request.POST.items():
                if input_name == 'csrfmiddlewaretoken':
                    continue
                else:
                    data = json.dumps(input_value, ensure_ascii=False)
                    field = json.dumps(input_name, ensure_ascii=False)
                    UserModel.objects.create(user_data=data, user_field=field)
            return redirect('dynamicform:done_form')
    else:
        form = UserForm()

    context = {
        'form': form
    }

    return render(request, 'dynamicform/dynamicform.html', context)


def done_form(request):
    form_objects = [
        [index.user_field.replace ('"', ' '), index.user_data.replace ('"', ' ')]
        for index in UserModel.objects.all()
    ]

    UserModel.objects.all().delete()

    context = {
        'form_objects': form_objects,
    }

    return render(request, 'dynamicform/done.html', context)
