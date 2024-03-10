from settings import env_templates
from http import HTTPStatus


def login_page(request):
    header = f'HTTP/1.1 {HTTPStatus.OK} OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n'
    template_name = 'login.html'
    template = env_templates.get_template(template_name)
    response = template.render()
    method = request.split()[0]
    if method == 'POST':
        form_data = request.split('\r\n\r\n')[1]
        username, password = form_data.split('&')
        username = username.split('=')[1]
        password = password.split('=')[1]

        ...

        return header.encode('UTF-8') + response.encode('UTF-8')
    return header.encode('UTF-8') + response.encode('UTF-8')


def not_found_page(request):
    header = f'HTTP/1.1 {HTTPStatus.NOT_FOUND} NOT FOUND\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n'
    template_name = 'not_found_404.html'
    template = env_templates.get_template(template_name)
    response = template.render()
    return header.encode('UTF-8') + response.encode('UTF-8')
