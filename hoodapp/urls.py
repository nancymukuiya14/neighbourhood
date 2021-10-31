from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns=[
    path('',views.home,name='home'),
    url(r'^new/business$',views.new_business,name='new-business'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^new_profile/$',views.new_profile,name = 'new_profile'),
    url(r'^edit/profile/$',views.profile_edit,name = 'edit_profile'),
    url(r'business_list/$',views.business,name='business'),
    url(r'^search/',views.search_post, name='search_results'),
    url(r'contact-us/$',views.contact, name='contact-us'),
    url(r'new_post/$',views.new_post,name='create-post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)