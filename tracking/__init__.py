from django.conf import settings
from django.core.urlresolvers import reverse, NoReverseMatch

VERSION = (0, 3, 0)

def get_version():
    "Returns the version as a human-format string."
    return '.'.join([str(i) for i in VERSION])

# initialize the URL prefixes that we shouldn't track
prefixes = getattr(settings, 'NO_TRACKING_PREFIXES', [])
if '!!initialized!!' not in prefixes:
    if settings.MEDIA_URL and settings.MEDIA_URL != '/':
        prefixes.append(settings.MEDIA_URL)

    if settings.ADMIN_MEDIA_PREFIX:
        prefixes.append(settings.ADMIN_MEDIA_PREFIX)

    try:
        # finally, don't track requests to the tracker update pages
        prefixes.append(reverse('tracking-refresh-active-users'))
    except NoReverseMatch:
        # django-tracking hasn't been included in the URLconf if we get here
        pass

    prefixes.append('!!initialized!!')

    settings.NO_TRACKING_PREFIXES = prefixes
