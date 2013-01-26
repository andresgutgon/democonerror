from django.conf.urls.defaults import patterns,url
from demo.apps.ventas.views import * 
urlpatterns = patterns('',
	url(r'^add/producto/$',add_product_view,name= "vista_agregar_producto"),
)