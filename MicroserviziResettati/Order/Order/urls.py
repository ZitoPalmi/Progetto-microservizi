from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Ordini import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.OrderList.as_view()),
    path('<int:borrowing_id>/', views.OrderGet.as_view()),
    path("create/", views.OrderCreate.as_view(), name="Order_create"),
    path("update/<int:pk>/", views.OrderUpdate.as_view(), name="update_Order"),
    path("delete/<int:pk>/", views.OrderDelete.as_view(), name="delete_Order"),
]


urlpatterns = format_suffix_patterns(urlpatterns)