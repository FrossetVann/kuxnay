from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.indexpage.as_view(), name='home'),
    path('categories', views.categories.as_view(), name='categories'),
    path('accounts', views.accounts, name='accounts'),
    path('authorization', views.authorization.as_view(), name='authorization'),
    path('login', views.login.as_view(), name='login'),
    path('logout', views.logoutuser, name='logout'),
    path('<int:pk>', views.recipedetail.as_view(), name='recipe')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
