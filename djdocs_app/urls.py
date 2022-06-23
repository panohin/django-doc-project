from django.urls import path

from . import views

app_name = 'djdocs_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index_url'),
    path('<int:pk>', views.DetailView.as_view(), name='detail_url'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results_url'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
