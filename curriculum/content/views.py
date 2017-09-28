from django.views.generic.base import View, TemplateResponseMixin


class IndexView(TemplateResponseMixin, View):
    template_name = 'content/index.html'

    def get(self, request, *args, **kwargs):

        return self.render_to_response({
            'message': 'Hola!',
        })
