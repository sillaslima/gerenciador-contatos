from django.urls import path
from gerirContatos import views
urlpatterns = [
    path('',views.ApiRoot.as_view()),
    path('listar-canais/', views.CanalContatoViewSet.as_view()),
    path('contato/list', views.ContatosViewSet.as_view()),
    path('contato/update/<int:pk>', views.ContatoUpdateViewSet.as_view()),
    path('contato/detail/<int:pk>', views.ContatoDetailViewSet.as_view()),
    path('contato/create/', views.ContatoCreateViewSet.as_view()),
    path('contato/delete/<int:pk>', views.ContatoDeleteViewSet.as_view())
]

