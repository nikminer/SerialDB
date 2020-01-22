from django import template

from Main.models import UserList
from Profile.models import Friendlist

register = template.Library()

@register.inclusion_tag("Serials/blocks/Friends.html")
def friendListS(profile,season):
    return {
        'friends': UserList.objects.filter(
            user__in=Friendlist.friends.get_friends(profile),
            season=season
        ).order_by('user__first_name')
    }
