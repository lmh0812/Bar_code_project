from django.contrib import admin
from django.urls import path
from main import views


app_name = 'main' # 템플릿에서 url로 사용하기 위함
urlpatterns = [
    # path('', views.home),
    # path('product/', views.product),
    # path('main/insert/', views.insert),
    path('', views.index, name = 'index'),
    # ex: /main/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /main/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('home/', views.home, name = 'home'),
    # path('home/insert/<int:code_id>', views.insert, name = 'insert'),
    # path('home/ins/', views.ins, name = 'ins'),
    path('home/add/', views.add, name='add'),
    path('home/<int:code_id>/', views.post_detail, name='post_detail'), # code_id란 변수로 view에 넘겨주기
    path('home/<int:code_id>/edit/', views.post_edit, name='post_edit'), 
    path('home/<int:code_id>/delete', views.post_delete, name='post_delete'),

    path('upload/', views.upload_image, name='upload_image'),
    path('upload/<int:img_id>/', views.img_detail, name='img_detail'),
    path('home/img_add', views.img_add, name="img_add"),
]