from django.urls import path

from frontpage import views

app_name = 'frontpage'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='frontpage'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
