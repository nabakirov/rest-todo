from rest_framework_simplejwt import views as jwt_views
from user import views
from django.urls import path


urlpatterns = [
    path('v1/login/', views.LoginViewSet.as_view(), name='login'),
    path('v1/registration/', views.RegistrationViewSet.as_view(), name='registration'),
    path('v1/refresh_token/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/profile/', views.GetUserView.as_view()),
]
