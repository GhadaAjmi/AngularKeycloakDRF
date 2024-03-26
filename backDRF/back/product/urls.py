from django.urls import path
from . import views
from django.utils.decorators import method_decorator


urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='products'),


]