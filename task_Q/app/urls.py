from django.urls import path
# from app import views
from . import views
urlpatterns = [
    path('a',views.fun1),
    path('b',views.fun2),
    path('index',views.index_page),
    path('fun3/<a>/<b>',views.fun3),
    path('fun4/<int:a>/<int:b>/<int:c>',views.fun4),
    path('bonus/<int:a>/<int:b>',views.bonus),
    path('divisable/<int:a>',views.divisable),
    path('bill/<int:a>',views.bill),
    path('city/<str:a>',views.city),
    path('tax/<int:a>',views.tax),
    path('day/<int:a>',views.day)
]