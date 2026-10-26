from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('update/<int:pk>/', views.RetriveUpdate.as_view(), name='event-crud'),
    path('list/', views.EventListCreate.as_view(), name='event-list'),
    path('gen/', views.EventListCreateMixin.as_view(), name='event-list-create'),
    path('detail/<int:pk>/', views.EventDetailMixin.as_view(), name='event-detail'),
    path('retrieve/<int:pk>/', views.EventListUpdateDelete.as_view(), name='event-detail-api'),
    path('create/', views.Create.as_view(), name='event-create'),

    path('api/token/', TokenObtainPairView.as_view(), name='jwt-token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='jwt-token-refresh'),

    path('event/', views.EventJWT.as_view(), name='jwt-event-api'),

    path('private/', views.PrivateView.as_view(), name='protected-event'),

    path('api-token-auth/', obtain_auth_token, name='token-auth'),
]