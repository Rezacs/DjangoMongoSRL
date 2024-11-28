from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers
from .models import Deck
from apps.cards.models import Card
from rest_framework import viewsets
from apps.cards.views import CardSerializer

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = "__all__"


class DecksViewSet(viewsets.ModelViewSet):
    serializer_class = DeckSerializer
    queryset = Deck.objects.all()

class DeckCardsViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

    def list(self, request, decks_pk):
        cards = Card.objects.filter(deck=decks_pk)
        serializer = self.get_serializer(cards, many=True)
        return Response(serializer.data)
