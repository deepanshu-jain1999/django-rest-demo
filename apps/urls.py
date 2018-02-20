from django.conf.urls import url, include
from apps import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'profile', views.ProfileViewSet, base_name='profile')
router.register(r'users', views.UserViewSet, base_name='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls)),

]






# urlpatterns = [
#     url(r'^users/$', views.UserList.as_view(), name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
#     url(r'^profile/$', views.ProfileList.as_view(), name='profile-list'),
#     url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileDetail.as_view(), name='profile-detail'),
# ]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),

]
