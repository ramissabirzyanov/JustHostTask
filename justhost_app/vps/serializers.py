from rest_framework.serializers import ModelSerializer
from justhost_app.vps.models import VPS


class VPSSerializer(ModelSerializer):

    class Meta:
        model = VPS
        fields = ['uid', 'cpu', 'ram', 'hdd', 'status']


class VPSStatusChangeSerializer(ModelSerializer):

    class Meta:
        model = VPS
        fields = ['status']
