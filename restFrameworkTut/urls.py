from django.conf.urls import include, url
from django.contrib import admin
from snippets import views
from rest_framework.routers import DefaultRouter


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the beowsable API


urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
