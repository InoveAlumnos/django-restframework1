from django.urls import path
from e_commerce.hello_world_views import *
from e_commerce.marvel_views import *


urlpatterns = [
    path('hello-world/', hello_world_view),
    path('request-data/', request_data_view),
    path('get-comics/', get_comics),
    path('purchased-item/', purchased_item),
]
