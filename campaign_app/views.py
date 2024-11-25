# campaign_app/views.py
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Agent, Campaign, CampaignResult
from .serializers import AgentSerializer, CampaignSerializer, CampaignResultSerializer

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class CampaignResultViewSet(viewsets.ModelViewSet):
    queryset = CampaignResult.objects.all()
    serializer_class = CampaignResultSerializer
