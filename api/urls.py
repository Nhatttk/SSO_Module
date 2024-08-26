
from django.conf.urls import include
from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework import permissions

from .serializers import MyTokenObtainPairView
from .views import *


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

history_log_get_all_api = HistoryLogMVS.as_view(
    {'get': 'history_log_get_all_api'})
upload_avatar_user_api = UploadAvatarUserMVS.as_view(
    {'patch': 'upload_avatar_user_api'})
profile_check_exist_api = ProfileMVS.as_view(
    {'post': 'profile_check_exist_api'})
profile_add_api = ProfileMVS.as_view({'post': 'profile_add_api'})

get_all_user_profile = UserProfileViewSet.as_view(
    {'get': 'get_all_user_profile'})

urlpatterns = [
    # user
    path('account/get-user-profile/', get_profile_view),
    path('account/update-user-profile/', update_user_profile_view),
    path('account/change-password/', change_password_view),
    path('account/history-log-get-all/', history_log_get_all_api),
    path('account/upload-avatar-user/', upload_avatar_user_api),
    path('account/profile-check-exist/', profile_check_exist_api),
    path('account/profile-add/', profile_add_api),
    path('account/logout/', logout),

    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

    path('get_all_user_profile/', get_all_user_profile),
    # auth
    path('auth/google/', GoogleView.as_view(), name='google'),
    path('auth/login/', MyTokenObtainPairView.as_view()),
    # #
    path('system/', include('api.system.urls')),

    # get token 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('check-token/', CheckTokenView.as_view(), name='check-token'),

     # GET URL TO DISPLAY GOOGLE LOGIN VIEW 
    path('auth/google-login/', LoginCustomView.as_view(), name='login_google_custom'),
    # AUTHENTICATE GOOGLE AND RESPONSE TOKEN DATA TO SATELLITE SYSTEM 
    path('auth/get_token_from_google_authenticate/', get_token_from_google_authenticate, name='get_token_from_google_authenticate'),
    # path('google-logout/', logout_view, name='logout'),
]
