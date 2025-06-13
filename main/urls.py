from django.urls import path
from .views import (
    HomeView, KorxonaListView, KorxonaCreateView,
    KorxonaUpdateView, KorxonaDeleteView, ContactView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('korxonalar/', KorxonaListView.as_view(), name='korxona_list'),
    path('korxonalar/add/', KorxonaCreateView.as_view(), name='korxona_add'),
    path('korxonalar/edit/<int:pk>/', KorxonaUpdateView.as_view(), name='korxona_edit'),
    path('korxonalar/delete/<int:pk>/', KorxonaDeleteView.as_view(), name='korxona_delete'),
    path('contact/', ContactView.as_view(), name='contact'),
]
