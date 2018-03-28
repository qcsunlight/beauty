from django.conf.urls import url
from server import views as view

urlpatterns = [
	#url(r'^$', view.index_view),
	url(r'^upload/$', view.upload_view),
]