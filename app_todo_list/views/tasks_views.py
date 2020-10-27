from app_todo_list.serializers import TasksSerializer
from .generic_views import GenericList, GenericDetail


class TasksList(GenericList):
    serializer_class = TasksSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class TaskDetail(GenericDetail):
    serializer_class = TasksSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
