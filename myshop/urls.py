"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += i18n_patterns(
    url(r'^admin/', admin.site.urls),
    url(_(r'^cart/'), include(('cart.urls', 'cart'), namespace='cart')),
    url(_(r'^orders/'), include(('orders.urls', 'orders'), namespace='orders')),
    url(_(r'^payment/'), include(('payment.urls', 'payment'), namespace='payment')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(_(r'^coupons/'), include(('coupons.urls', 'coupons'), namespace='coupons')),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^', include(('shop.urls', 'shop'), namespace='shop')),

)

# urlpatterns = [
#         url(r'^admin/', admin.site.urls),
#         url(_(r'^cart/'), include(('cart.urls', 'cart'), namespace='cart')),
#         url(_(r'^orders/'), include(('orders.urls', 'orders'), namespace='orders')),
#         url(_(r'^payment/'), include(('payment.urls', 'paymrarrent'), namespace='payment')),
#         url(r'^paypal/', include('paypal.standard.ipn.urls')),
#         #url(r'^paypal/', include(('paypal.standard.ipn.urls', 'paypal'), namespace='paypal-ipn')),
#         url(_(r'^coupons/'), include(('coupons.urls', 'coupons'), namespace='coupons')),
#         url(r'^rosetta/', include('rosetta.urls')),
#         url(r'^', include(('shop.urls', 'shop'), namespace='shop')),
# ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)