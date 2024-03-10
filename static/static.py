from http import HTTPStatus


def get_static_by_request(request):
    header = f'HTTP/1.1 {HTTPStatus.OK} OK\nContent-Type: text/css\n\n'
    path_to_file = request.split(' ')[1]

    if path_to_file.startswith('/static/'):
        with open(f'{path_to_file[1:]}', 'rb') as file:
            response = file.read()
        return header.encode('UTF-8') + response
