from rest_framework import serializers
from topit.models import Magic


class MagicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magic
        fields = "__all__"
