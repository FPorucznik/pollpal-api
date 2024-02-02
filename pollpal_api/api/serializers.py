from rest_framework import serializers
from .models import Option, Poll, Vote


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


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['option', 'user_ip']

    def validate(self, data):
        option = data.get('option')
        user_ip = data.get('user_ip')

        if option:
            poll = option.poll
            poll_options = poll.options.all()

            for poll_option in poll_options:
                existing_vote = poll_option.votes.all().filter(user_ip=user_ip)
                if existing_vote:
                    raise serializers.ValidationError('The user has already voted in this poll')
        return data

    def create(self, validated_data):
        print(validated_data)
        option = validated_data.get('option')
        vote = Vote.objects.create(option=option, user_ip=validated_data.get('user_ip'))
        return vote
