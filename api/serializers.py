from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Issue,StillPresent

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
    

class IssueSerializer(serializers.ModelSerializer):

    still_present_count = serializers.CharField(read_only=True)

    reacted = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = Issue

        fields = '__all__'

        read_only_fields = ('id','owner','created_at','updated_at')

    def get_reacted(self,object):

        # We have to fetch all users those who reacted current issue object.
        # Here issue object is object
        
        users_list = StillPresent.objects.filter(issue = object).values_list('owner',flat=True)

        print(users_list)

        print(self.context.get('user'))

        if self.context.get('user') in users_list:

            return True
        
        else:

            return False

