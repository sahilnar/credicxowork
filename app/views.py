from rest_framework import viewsets, mixins, permissions
from .serializers import TeacherSerializer
from .models import Teacher


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('studentname')
    serializer_class = TeacherSerializer

class StudentViewSet(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    