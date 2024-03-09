def login_page(request):
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n'
    template_name = 'templates/login.html'
    with open(template_name, 'rb') as file:
        response = file.read()
    return header.encode('UTF-8') + response


def not_found_page(request):
    header = 'HTTP/1.1 404 NOT FOUND\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n'
    template_name = 'templates/not_found_404.html'
    with open(template_name, 'rb') as file:
        response = file.read()
    return header.encode('UTF-8') + response
