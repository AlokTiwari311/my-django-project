# campaign_app/serializers.py
from rest_framework import serializers
from .models import Agent, Campaign, CampaignResult

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id', 'agent_name', 'language', 'voice_id', 'updated']

class CampaignSerializer(serializers.ModelSerializer):
    agent = AgentSerializer()  # Nested serializer for agent

    class Meta:
        model = Campaign
        fields = ['id', 'campaign_name', 'type', 'phone_number', 'status', 'agent']

    def create(self, validated_data):
        agent_data = validated_data.pop('agent')
        # Create the agent first
        agent = Agent.objects.create(**agent_data)
        # Now create the campaign
        campaign = Campaign.objects.create(agent=agent, **validated_data)
        return campaign

class CampaignResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignResult
        fields = ['id', 'name', 'result_type', 'phone', 'cost', 'outcome', 'call_duration', 'recording', 'summary', 'transcription']
