from rest_framework import serializers


class BookReviewSerializer(serializers.Serializer):
    stars_given = serializers.IntegerField(min_value=1, max_value=5)
    comment = serializers.CharField()
