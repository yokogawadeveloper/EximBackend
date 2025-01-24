from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import *


# Create your views here.
class MasterItemBatchViewSet(viewsets.ModelViewSet):
    queryset = MasterItem.objects.prefetch_related('inline_items')
    serializer_class = MasterItemBatchSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(is_active=True)


class InlineItemViewSet(viewsets.ModelViewSet):
    queryset = InlineItem.objects.all()
    serializer_class = InlineItemSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return InlineItem.objects.filter(is_active=True)
