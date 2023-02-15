from django.shortcuts import render


def example_view(req):
    # my_app/templates/my_app/example.html
    return render(req, 'my_app/example.html')


def variable_view(req):
    my_var = {
        # 字符串变量
        'first_name': 'Rosalind',
        'last_name': 'Franklin',
        # list变量
        'some_list': [1, 2, 3],
        # 字典变量
        'some_dict': {
            'inside_key': 'inside_value'
        },
        # bool
        'user_logged_in': True
    }
    # context是上下文对象,在模板文件里可以拿到
    return render(req, 'my_app/variable.html', context=my_var)
