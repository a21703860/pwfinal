
from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path("", views.index, name="index"),
    path("sections/<int:num>", views.section, name="section"),


    path('home', views.home_page_view, name='home'),
    path('musica', views.musica_page_view, name='musica'),
    path('Toys', views.Toys_page_view, name='Toys'),
    path('sobre', views.sobre_page_view, name='sobre'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('quinta', views.quinta_page_view, name='quinta'),
    path('jogos', views.jogos_page_view, name='jogos'),
    path('comentarios/', views.novo_comentario_view, name='comentarios'),

    path('nova/', views.nova_tarefa_view, name='nova'),
    path('contactos/', views.contactos_page_view, name='contactos'),
    path('edita/<int:contacto_id>', views.edita_tarefa_view, name='edita'),
    path('apaga/<int:contacto_id>', views.apaga_tarefa_view, name='apaga')
]