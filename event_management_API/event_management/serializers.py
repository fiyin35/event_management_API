from rest_framework import serializers
from .models import Events, Attendees


class EventsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Events # model to serialize
        fields = ['id', 
                  'event_title', 
                  'event_description', 
                  'event_date_and_time', 
                  'event_location', 
                  'event_organizer', 
                  'event_capacity', 
                  'created_at', 
                  'created_by'
                  'updated_at'
                  ]
        read_only_fields = ['created_at', 'created_by', 'updated_at']
        



class AttendeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attendees
        fields = ['id', 'name', 'email', 'phone_number', 'event']
