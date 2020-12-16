from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('prod_det_1/', views.prod_det_1, name="prod_det_1"),
    path('prod_det_2/', views.prod_det_2, name="prod_det_2"),
    path('prod_det_3/', views.prod_det_3, name="prod_det_3"),
]