from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
