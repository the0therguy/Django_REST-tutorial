from django.urls import path
from .views import *

urlpatterns = [
    path('article/', article_list),
    path('', ArticleApiView.as_view()),
    path('ad/<int:pk>/', article_detail),
    path('a/<int:id>/', ArticleDetailView.as_view()),
    path('gattt/<int:id>/', GenericAPIView.as_view()),
]
