from django.conf.urls import url
from dados import views

urlpatterns = [
    url(r'^api/dados$', views.dados_list),
    url(r'^api/dados/(?P<pk>[0-9]+)$', views.dado_detail)
]