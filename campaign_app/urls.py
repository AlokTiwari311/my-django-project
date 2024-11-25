# campaign_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'agents', views.AgentViewSet)
router.register(r'campaigns', views.CampaignViewSet)
router.register(r'campaign-results', views.CampaignResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
