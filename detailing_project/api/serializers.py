from rest_framework import serializers
from .models import Order, Client, Service, Master


class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = ["id", "first_name", "last_name", "specialization"]


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "name", "description", "price"]


class OrderSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    services = ServiceSerializer(many=True)
    master = MasterSerializer()

    class Meta:
        model = Order
        fields = ["id", "client", "services", "master", "status", "notes"]

    def create(self, validated_data):
        client_data = validated_data.pop("client")
        services_data = validated_data.pop("services")
        master_data = validated_data.pop("master")

        client = Client.objects.create(**client_data)
        master = Master.objects.create(**master_data)
        order = Order.objects.create(client=client, master=master, **validated_data)

        for service_data in services_data:
            service = Service.objects.create(**service_data)
            order.services.add(service)

        return order
