from django.conf.urls import url
from views import ProductListView, ProductDetailView

urlpatterns = [

    url(r'^(?P<pk>[\w]+)/$', ProductDetailView.as_view(), name='product-detail'),
    url(r'^$', ProductListView.as_view(), name='product-list' ),
    #url(r'^(?P<pk>[-\w]+)/$',ProductEditView.as_view(), name='product_edit'),
    # url(r'^(?P<pk>[-\w]+)/$', ProductListView.as_view(), name='product-list'),

]
