import urlparse
import urllib
import uuid
import hashlib
import hmac
import base64
import urllib2
import time
import json
import gzip
import os
import cookielib
from StringIO import StringIO

import xbmc
from globals import ADDON_PATH_PROFILE

from adobe import adobe_activate_api

TAG = 'ESPN3-adobe-api: '

espn_adobe = adobe_activate_api.AdobeActivateApi('ESPN', 'yKpsHYd8TOITdTMJHmkJOVmgbb2DykNK', 'gB8HYdEPyezeYbR1')
def deauthorize():
    espn_adobe.deauthorize()

def get_short_media_token(resource):
    return espn_adobe.get_short_media_token(resource)

def is_authenticated():
    return espn_adobe.is_authenticated()

def get_resource(channel, event_name, event_guid, event_parental_rating):
    return adobe_activate_api.get_resource(channel, event_name, event_guid, event-event_parental_rating)
