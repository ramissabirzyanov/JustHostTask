from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import VPSSerializer, VPSStatusChangeSerializer
from .models import VPS


class VPSListView(ListAPIView):
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cpu', 'ram', 'hdd', 'status']


class VPSCreateView(CreateAPIView):
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer


class VPSDetailView(APIView):

    def get_object(self, uid):
        try:
            return VPS.objects.get(uid=uid)
        except VPS.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, uid, format=None):
        current_vps = self.get_object(uid)
        serializer = VPSSerializer(current_vps)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, uid, format=None):
        current_vps = self.get_object(uid)
        serializer = VPSStatusChangeSerializer(current_vps, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
