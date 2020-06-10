from django.urls import path
from snippets import views
from rest_framework.routers import SimpleRouter
from snippets.views import SnippetViewSet

router = SimpleRouter()
router.register(r'snippets', SnippetViewSet, basename='Snippet')

urlpatterns = router.urls

# urlpatterns = [
#     path('snippets/', views.SnippetList.as_view()),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
# ]
