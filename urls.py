import views


class UrlDispatcher:
    def __init__(self):
        self.urlpatterns = {
            '/login': views.login_page,
            '/registration': views.registration_page,
            '/index': views.index_page,
        }

    def get_template_by_request(self, request):
        urlpattern = request.split(' ')[1]
        if '?' in urlpattern:
            urlpattern, parameters = urlpattern.split('?')

        if self.is_exist_urlpattern(urlpattern):
            view = self.get_view_by_urlpattern(urlpattern)
        else:
            view = views.not_found_page

        content = view(request)
        return content

    def get_view_by_urlpattern(self, urlpattern):
        return self.urlpatterns.get(urlpattern)

    def is_exist_urlpattern(self, urlpattern):
        return urlpattern in self.urlpatterns
