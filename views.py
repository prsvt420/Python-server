from http import HTTPStatus

import bcrypt
from sqlalchemy import exists

import models
from settings import env_templates


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

        with models.UserModelSession() as user_model:
            user = user_model.query(models.User).filter_by(username=username).first()

            if user and bcrypt.checkpw(password.encode('UTF-8'), user.password):
                header = f'HTTP/1.1 {HTTPStatus.FOUND} FOUND\r\nLocation: /index\r\n\r\n'
                return header.encode('UTF-8')
    return header.encode('UTF-8') + response.encode('UTF-8')


def registration_page(request):
    header = f'HTTP/1.1 {HTTPStatus.OK} OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n'
    template_name = 'registration.html'
    template = env_templates.get_template(template_name)
    response = template.render()
    method = request.split()[0]
    if method == 'POST':
        form_data = request.split('\r\n\r\n')[1]
        username, password_1, password_2 = form_data.split('&')
        username = username.split('=')[1]
        password_1 = password_1.split('=')[1]
        password_2 = password_2.split('=')[1]

        with models.UserModelSession() as user_model:
            user_is_exist = user_model.scalar(exists().where(models.User.username == f'{username}').select())

            if not user_is_exist and password_1 and password_1 == password_2:
                header = f'HTTP/1.1 {HTTPStatus.FOUND} FOUND\r\nLocation: /login\r\n\r\n'
                password = bcrypt.hashpw(password_1.encode('UTF-8'), bcrypt.gensalt())
                user = models.User(username=username, password=password)
                user_model.add(user)
                user_model.commit()
                return header.encode('UTF-8')
    return header.encode('UTF-8') + response.encode('UTF-8')


def index_page(request):
    header = f'HTTP/1.1 {HTTPStatus.OK} OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n'
    template_name = 'index.html'
    template = env_templates.get_template(template_name)
    response = template.render()
    return header.encode('UTF-8') + response.encode('UTF-8')


def not_found_page(request):
    header = f'HTTP/1.1 {HTTPStatus.NOT_FOUND} NOT FOUND\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n'
    template_name = 'not_found_404.html'
    template = env_templates.get_template(template_name)
    response = template.render()
    return header.encode('UTF-8') + response.encode('UTF-8')
