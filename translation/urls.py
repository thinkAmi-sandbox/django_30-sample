from django.urls import path
from django.views.generic import TemplateView


app_name = 'translation'
urlpatterns = [
    path('', TemplateView.as_view(template_name='translation/index.html'), name='index'),
]
