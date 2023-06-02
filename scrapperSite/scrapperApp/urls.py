from django.urls import path

from . import views
urlpatterns = [
    path('update_data/', views.update_data, name='update_data'),
    path('get_data/', views.get_latest_data, name='get_latest_data'),
]
