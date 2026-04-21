from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Serializers

class CustomTokenSerializer(TokenObtainPairSerializer) :

    def validate(self, attrs) :

        data = super().validate(attrs)
        custom_data = {
            "username" :self.user.username
        }
        data.update(custom_data)

        return data