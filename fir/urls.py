from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_method, name = 'home'), 
    path('create_draft/', views.create_draft_method, name = 'create_draft'), 
    path('update_draft/<int:id>', views.update_draft_method, name = 'update_draft'),
    path('update_draft_lebel/<int:id>', views.update_draft_label_method, name = 'update_draft_label'),
    path('delete_draft/<int:id>', views.delete_draft_method, name = 'delete_draft'),
    path('report/', views.report_method, name = 'report'), 
    path('report/<int:id>', views.report_method, name = 'report_id'), 
]
