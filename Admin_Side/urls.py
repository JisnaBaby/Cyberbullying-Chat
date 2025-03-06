from django.urls import path
from Admin_Side import views

urlpatterns = [
    path('',views.indexpage,name="indexpage"),
    path('display_user/',views.display_user,name="display_user"),
    path('display_complaint/',views.display_complaint,name="display_complaint"),
    path('display_contact/',views.display_contact,name="display_contact"),
    path('warned_users_page/', views.warned_users_page, {'count': 1}, name='warned_users_page'),
    path('warned_users_page/<int:count>/',views.warned_users_page,name="warned_users_page"),

]