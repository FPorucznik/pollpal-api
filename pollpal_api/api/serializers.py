from rest_framework import serializers
from .models import Option, Poll

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text']

class PollSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
    class Meta:
        model = Poll
        fields = '__all__'
    
    def validate_options(self, options):
        if len(options) >= 2:
            return options
        else:
            raise serializers.ValidationError('The poll must include at least 2 options to vote on')
    
    def create(self, validated_data):
        options_data = validated_data.pop('options')
        poll = Poll.objects.create(**validated_data)
        for option in options_data:
            Option.objects.create(poll=poll, **option)
        return poll