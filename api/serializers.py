from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(write_only=True)

    password2 = serializers.CharField(write_only=True)

    class Meta:

        model = User

        fields = ['id','username','email','password','password1','password2']

        read_only_fields = ('password',)


    def create(self, validated_data):

        password1 = validated_data.pop('password1')

        password2 = validated_data.pop('password2')
        
        return User.objects.create_user(**validated_data,password=password1)
    
    def validate(self, data):
        
        # validated_data = super().validate()

        password1 = data.get('password1')

        password2 = data.get('password2')

        if password1 != password2: # != not equal to

            raise serializers.ValidationError("Password field doesn't match")
        
        return data