from django.urls import path 
from  .views import SnackListView,SnackDetailView,SnackCreateView,SnackUpdateView,SnackDeleteView
urlpatterns = [
    
    path('',SnackListView.as_view(),name='thing_list'),
    path('<int:pk>/',SnackDetailView.as_view(),name='thing_detail'),
    path('create/',SnackCreateView.as_view(),name='thing_create'),
    path('update/<int:pk>',SnackUpdateView.as_view(), name='thing_update'),
    path('delete/<int:pk>',SnackDeleteView.as_view(), name='thing_delete')
    
]