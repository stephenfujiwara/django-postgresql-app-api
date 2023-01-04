from django.urls import path, include
from .views import ImageView, ImageViewDetail, UserImagesView, UserImagesViewDetail

urlpatterns = [path('images/', ImageView.as_view()), path('images/<int:pk>', ImageViewDetail.as_view()), 
    path('images/user/', UserImagesView.as_view()), path('images/user/<int:pk>', UserImagesViewDetail.as_view())
]