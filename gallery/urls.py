from django.conf.urls.static import static
from . import views
from django.conf import settings
from django.conf.urls import url


urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    # url(r'^search/', views.search_results, name = 'search_results'),
    # url(r'^categories/', views.display_images_categories, name = 'categories'),
    # url(r'^locations/', views.display_images_locations, name = 'locations'),

]