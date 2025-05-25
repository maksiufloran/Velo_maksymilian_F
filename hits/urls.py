from django.urls import path
from .views import HitListCreateView, HitDetailView

urlpatterns = [
    path('api/v1/hits', HitListCreateView.as_view(), name='hit-list-create'),
    path('api/v1/hits/<slug:title_url>', HitDetailView.as_view(), name='hit-detail'),
]
