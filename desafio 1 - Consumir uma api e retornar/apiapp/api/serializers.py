from rest_framework.serializers import ModelSerializer
from ..models import GithubModel

class GithubSerializer(ModelSerializer):
    class Meta:
        model = GithubModel
        fields = '__all__'