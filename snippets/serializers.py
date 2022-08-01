from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
class SnippetSerializer(serializers.Serializer):
    class Meta:
        model = Snippetfields = ['id', 'title', 'code', 'linenos', 'language', 'style']
    
    def create(self, validated_data):
        return Snippet.object.create(**validated_data)
    
    def update(self, instance, validated_data):
        #유효한 데이터가 들어오면 스니펫 인스턴스를 업데이트하고 반환
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code',instance.code)
        instance.lineos = validated_data.get('linenos',instance.linenos)
        instance.language = validated_data.get('language',instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
    
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(meny=True, queryset=Snippet.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
        
owner = serializers.ReadOnlyField(source='owner.username')