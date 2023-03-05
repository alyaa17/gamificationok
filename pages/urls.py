from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('history/history1/', views.history1_page_view, name='history1_view'),
    path('history/history2/', views.history2_page_view, name='history2_view'),
    path('history/history3/', views.history3_page_view, name='history3_view'),
    path('history/history4/', views.history4_page_view, name='history4_view'),
    path('history/history5/', views.history5_page_view, name='history5_view'),
    path('history/history6/', views.history6_page_view, name='history6_view'),
    path('history/history7/', views.history7_page_view, name='history7_view'),
    path('history/history8/', views.history8_page_view, name='history8_view'),

    path('quizzes/', views.quizzes_page_view, name='quizzes_view'),

    path('articles/', views.articles_page_view, name='articles_view'),
    path('articles/article1/', views.articles_page_view1, name='article1_view'),
    path('articles/article2/', views.articles_page_view2, name='article2_view'),
    path('articles/article3/', views.articles_page_view3, name='article3_view'),
    path('articles/article4/', views.articles_page_view4, name='article4_view'),
    path('articles/article5/', views.articles_page_view5, name='article5_view'),
    path('articles/article6/', views.articles_page_view6, name='article6_view'),
    path('articles/article7/', views.articles_page_view7, name='article7_view'),


    path('account/', views.account_page_view, name='account_view'),


]

