from django.urls import path
from .views import CreateAccountView
from .views import ProfileView

urlpatterns = [
    path('createaccount/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/', ProfileView.as_view(), name='profile')
]
