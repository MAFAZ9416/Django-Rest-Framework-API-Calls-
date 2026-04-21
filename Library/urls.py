from django.urls import path,include
from .router import *
from .views import *

# Urls

urlpatterns =[
    path('api/', include(library_router.urls)),
    path('laptop/',LaptopView.as_view()),
    path('laptop/<int:pk>/', LaptopViewById.as_view())
]