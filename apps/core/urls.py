from django.urls import path

from .views import index
# from .views import dashboard
# from .views import home

urlpatterns = [
    path('', index, name="index"),
    # path('home/', home, name="home"),
    # path('dashboard/', dashboard, name="dashboard"),
]
