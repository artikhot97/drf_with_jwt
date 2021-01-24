from rest_framework import serializers
from api.models import User, UserManager


class UserManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserManager
        fields = ('dob', 'address', 'company')


class UserSerializer(serializers.ModelSerializer):
    manger = UserManagerSerializer()

    """
    However UserSerializer is a bit more complicated. Because we need the UserManger to be serialized/deserialized as 
    part of the User model we created a Writable Nested Serializer as defined in the DRF documentation. 
    That is, a serializer that uses another serializer for a particular field ( manger in this case).
    """
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'manger')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        manger_data = validated_data.pop('manger')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserManager.objects.create(user=user, **manger_data)
        return user

    # def update(self, instance, validated_data):
    #     manger_data = validated_data.pop('manger')
    #     manger = instance.manger

    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()

    #     manger.title = manger_data.get('company', manger.title)
    #     manger.dob = manger_data.get('dob', manger.dob)
    #     manger.address = manger_data.get('address', manger.address)
    #     manger.save()

    #     return instance

class UserMangerCreateSerializer(serializers.ModelSerializer):
    manger = UserManagerSerializer()

    """
    However UserSerializer is a bit more complicated. Because we need the UserManger to be serialized/deserialized as 
    part of the User model we created a Writable Nested Serializer as defined in the DRF documentation. 
    That is, a serializer that uses another serializer for a particular field ( manger in this case).
    """
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'manger')
        extra_kwargs = {'password': {'write_only': True}}

