from django.urls import path
from .views import PasteView, PasteDetail, PasteList, PasteUpdate, PasteDelete

urlpatterns= [
    path('', PasteView.as_view(), name='pastebin_paste_create'),
    path('pastes/', PasteList.as_view(), name='pastebin_paste_list'),
    path('paste/<int:pk>/', PasteDetail.as_view(), name='pastebin_paste_detail'),
    path('paste/delete/<int:pk>/', PasteDelete.as_view(), name='pastebin_paste_delete'),
    path('paste/update/<int:pk>/', PasteUpdate.as_view(), name='pastebin_paste_update'),

]