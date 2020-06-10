from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from snippets.serializers import SnippetModelSerializer
from snippets.models import Snippet
from django_filters import rest_framework as filters

# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
# from rest_framework import filters

# from rest_framework.authtoken.models import Token
#
#
#

class SnippetFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")
    startswith_title = filters.CharFilter(field_name="code", method="filter_start")

    def filter_start(self, queryset, name, value):
        title_filter = {f'{name}__startswith': value}
        return queryset.filter(**title_filter)

    class Meta:
        model = Snippet
        fields = ('code',)


class SnippetViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetModelSerializer
    queryset = Snippet.objects.all()
    authentication_classes = [TokenAuthentication]
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_class = SnippetFilter


#     # Token = Token.objects.create(user=bunnycast)
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#     def list(self, request):
#         queryset = Snippet.objects.all()
#         serializer = SnippetSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self, request, pk=None):
#         queryset = Snippet.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = SnippetSerializer(user)
#         return Response(serializer.data)
#
#     def update(self, request, pk=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self, request, pk=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#

# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetModelSerializer
#
#
#     def list(self, *args, **kwargs):
#         print(self.request.user.username)
#         return super().list(*args, **kwargs)
#
#     def get(self, request, *args, **kwargs):
#         print(request.user.username)
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetModelSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
