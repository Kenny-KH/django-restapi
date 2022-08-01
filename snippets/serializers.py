from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template':'textarea.html'})
    lineos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    
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