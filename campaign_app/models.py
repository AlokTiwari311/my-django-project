# campaign_app/models.py
from django.db import models

class Agent(models.Model):
    agent_name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    voice_id = models.CharField(max_length=100)  # Unique voice identifier
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.agent_name
# campaign_app/models.py
class Campaign(models.Model):
    CAMPAIGN_TYPES = [
        ('Inbound', 'Inbound'),
        ('Outbound', 'Outbound'),
    ]
    CAMPAIGN_STATUS = [
        ('Running', 'Running'),
        ('Paused', 'Paused'),
        ('Completed', 'Completed'),
    ]
    
    campaign_name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CAMPAIGN_TYPES)
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=10, choices=CAMPAIGN_STATUS)
    agent = models.ForeignKey(Agent, related_name='campaigns', on_delete=models.CASCADE)

    def __str__(self):
        return self.campaign_name
# campaign_app/models.py
class CampaignResult(models.Model):
    name = models.CharField(max_length=100)
    result_type = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    cost = models.FloatField()
    outcome = models.CharField(max_length=100)
    call_duration = models.FloatField()
    recording = models.URLField()
    summary = models.TextField()
    transcription = models.TextField()

    def __str__(self):
        return self.name
