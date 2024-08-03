from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # Path for registration
    path('register/', views.registration, name='registration'),

    # Path for login
    path('login/', views.login_user, name='login'),

    # Path for dealer reviews view
    path('dealerships/', views.get_dealerships, name='get_dealerships'),
    path('dealerships/<int:dealer_id>/reviews/', views.get_dealer_reviews, name='get_dealer_reviews'),

    # Path for add a review view
    path('reviews/add/', views.add_review, name='add_review'),

    # Path for dealer details view
    path('dealerships/<int:dealer_id>/', views.get_dealer_details, name='get_dealer_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
