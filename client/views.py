from django.template.response import TemplateResponse


def index(req, *args, **kwargs):
    return TemplateResponse(req, 'pages/index.html')


def robots(req, *args, **kwargs):
    return TemplateResponse(req, 'assets/robots.txt')

