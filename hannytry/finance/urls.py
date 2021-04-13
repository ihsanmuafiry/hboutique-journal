from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('ubah/<int:id>/',views.ubah,name='ubah'),
    path('hapus/<int:id>/', views.hapus, name='hapus'),
    path('detail/', views.detail, name='detail'),
]