from django.shortcuts import render
# 这里参数名必须是exception
def my_custom_page_not_found_view(req, exception):
    return render(req, 'error_view.html', status=404)
