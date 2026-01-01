from django.urls import path, re_path
from . import views

urlpatterns = [
    path('post/<int:post_id>/',views.post_details, name='post_details'),
    path('post/<str:username>/',views.user_profile, name='user_profile'),
    path('article/<int:year>/<int:month>/<int:day>/',views.article_kwargs, name='article-details'),

    re_path(r'^article/(?P<year>[0-9]{4})/$', views.article_by_year, name='articleByYear'),
]