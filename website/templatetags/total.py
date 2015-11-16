import datetime
from django import template
from website.models import UserProfile
from django.db.models import Sum

register = template.Library()

@register.simple_tag
def bounty_total():
	try:
		return "{:,.0f}".format(UserProfile.objects.aggregate(Sum('balance'))['balance__sum'])
	except ValueError, e:
		return 0
    