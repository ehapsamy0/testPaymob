from rest_framework.serializers import ModelSerializer,Serializer
from .models import Gug,User,Project






class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'




class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'






class GugSerializer(ModelSerializer):
    class Meta:
        model = Gug
        fields = '__all__'