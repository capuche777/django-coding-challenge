from django.urls import path

from . import views

app_name = "checkout"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("api", views.IndexView.as_view(), name="index"),
    path("api/products/", views.ProductListView.as_view({"get": "list"}), name="products",),
    path("api/products/<int:pk>/", views.ProductUpdateView.as_view(), name="product-update"),
    path("api/order/", views.OrderView.as_view(), name="order"),
]
