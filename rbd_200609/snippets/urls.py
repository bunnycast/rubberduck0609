from django.urls import include, path
from rest_framework.routers import SimpleRouter
from snippets.views import SnippetViewSet

router = SimpleRouter()
router.register(r'snippets', SnippetViewSet, basename='Snippet')

urlpatterns = [
    # path('', include(router.urls))
]

urlpatterns += router.urls
