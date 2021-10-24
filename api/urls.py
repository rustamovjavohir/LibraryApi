from django.urls import path
from .views import *

urlpatterns = [
    path('', BookApiView.as_view(), name='book_api'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail_api'),
    path('reader/', ReaderApiView.as_view(), name='reader_list'),
    path('reader/<int:pk>/', ReaderDetailView.as_view(), name='reader_detail_api'),
    path('kartoteka/', KartotekaListView.as_view(), name='kartoteka_list'),
    path('kartoteka/<int:pk>', KartotekaDetailView.as_view(), name='kartoteka_detail'),
    path('kartoteka/', KartotekaListView.as_view(), name='reader_books'),
    path('kartoteka/<int:pk>/update/', KartotekaUpdateView.as_view(), name='kartoteka_update')
]
