from django.shortcuts import render, redirect
from rest_framework.views import APIView
from apps.serializers import ProfileSerializer, UserSerializer
from apps.models import Profile
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from apps.permissions import IsOwnerOrReadOnly
# from django.urls import reverse_lazy
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.parsers import FormParser, MultiPartParser


# class ProfileViewSet(viewsets.ModelViewSet):
#     """
#        This viewset automatically provides `list`, `create`, `retrieve`,
#        `update` and `destroy` actions.
#
#        Additionally we also provide an extra `highlight` action.
#      """
#
#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = ProfileSerializer
#     lookup_field = 'slug'
#     # parser_classes = (FormParser, MultiPartParser)
#
#     def get_queryset(self):
#         user = self.request.user
#         return Profile.objects.filter(owner=user)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user,
#                         # datafile=self.request.data.get('datafile')
#                         )


class ProfileList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(owner=user)
#
#




# by using mixins
# class ProfileList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class ProfileDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#




# class ProfileList(APIView):
#
#     def get(self, request):
#         if not self.request.user.is_authenticated:
#             return redirect('/api-auth/login/')
#         else:
#             profile = Profile.objects.filter(owner=self.request.user)
#             serializer = ProfileSerializer(profile, many=True)
#             return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(owner=self.request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class ProfileDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly,)
#     def get_object(self, pk, user):
#         try:
#             return Profile.objects.get(pk=pk, owner=user)
#         except Profile.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         if not self.request.user.is_authenticated:
#             return redirect('/api-auth/login/')
#         user = self.request.user
#         profile = self.get_object(pk, user)
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         user = self.request.user
#         profile = self.get_object(pk, user)
#         serializer = ProfileSerializer(profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         user = self.request.user
#         profile = self.get_object(pk, user)
#         profile.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# *************USER BY VIEW******

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(username=user)


# class UserList(generics.ListAPIView):
#     serializer_class = UserSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         return User.objects.filter(username=user)
#
#
# class UserDetail(generics.RetrieveAPIView):
#     serializer_class = UserSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         return User.objects.filter(username=user)

