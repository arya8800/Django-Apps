from django.conf.urls import url
from django.contrib import admin
from gonextmedia.views import *

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^index/$',index),
	url(r'^kyc/$',kyc),
	url(r'^manage-compane/$', manage),
	url(r'^my-profile/$', myprofile),
	url(r'^network/$', network),
	url(r'^payouthistory/$', payout),
	url(r'^Promotional/$', promotional),
	url(r'^reffral/$', reffral),
	url(r'^rewards/$', rewards),
	url(r'^sales/$', sales),
	url(r'^today-task/$', todayt),
	url(r'front/',front),
	url(r'signup/',signup),

]
