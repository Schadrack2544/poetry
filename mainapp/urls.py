from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.poetry_list, name='poetry_list'),
    path('poetry/create/', views.PoetryPostCreateView.as_view(), name='poetry_create'),
    path('poetry/<int:pk>/', views.poetry_detail, name='poetry_detail'),
    path('poetry/<int:pk>/update/', views.PoetryPostUpdateView.as_view(), name='poetry_update'),
    path('poetry/<int:pk>/delete/', views.PoetryPostDeleteView.as_view(), name='poetry_delete'),
    path('photography/', views.photography_list, name='photography_list'),
    path('short-stories/',views.shortstories_list, name='short_stories_list'),
    path('opinions/', views.opinions_list, name='opinions-list'),
    path('poetry/', views.poetry_only, name='poetry_only'),
    path('photography/create/', views.PhotographyPostCreateView.as_view(), name='photography_create'),
    path('photography/<int:pk>/', views.photography_detail, name='photography_detail'),
    path('photography/<int:pk>/update/', views.PhotographyPostUpdateView.as_view(), name='photography_update'),
    path('photography/<int:pk>/delete/', views.PhotographyPostDeleteView.as_view(), name='photography_delete'),
    path('photography/<int:pk>/featured-images/', views.photography_featured_images, name='photography_featured_images'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)