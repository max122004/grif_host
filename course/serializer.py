from rest_framework import serializers

from course.models import Course, Category, Level


class CourseSerializer(serializers.ModelSerializer):
    level = serializers.CharField(source='get_level_display')

    class Meta:
        model = Course
        fields = ['title', 'image', 'level']


class CategoryListSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=True, read_only=True)
    # level = LevelSerializer()

    class Meta:
        model = Category
        fields = ['name', 'course']


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        course = super().create(validated_data)
        course.save()
        return course
