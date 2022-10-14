from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard_view),
    path('createBook/',views.create_book),
    path('detail/<int:book_id>',views.detail_view),
    path('update/<int:book_id>',views.update_book),
    path('delete/<int:book_id>',views.delete_book),
    path('detailNotLogin/<int:book_id>',views.notLogin_View),
    path('favorBook/<int:book_id>',views.favorBook)
]