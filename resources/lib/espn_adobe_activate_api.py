import adobe_activate_api

TAG = 'ESPN3-adobe-api: '

espn_adobe = adobe_activate_api.AdobeActivateApi('ESPN', 'yKpsHYd8TOITdTMJHmkJOVmgbb2DykNK', 'gB8HYdEPyezeYbR1')


def deauthorize():
    espn_adobe.deauthorize()


def get_short_media_token(resource):
    return espn_adobe.get_short_media_token(resource)


def is_authenticated():
    return espn_adobe.is_authenticated()


def get_resource(channel, event_name, event_guid, event_parental_rating):
    return adobe_activate_api.get_resource(channel, event_name, event_guid, event_parental_rating)


def reset_settings():
    espn_adobe.reset_settings()


def clean_up_authorization_tokens():
    espn_adobe.clean_up_authorization_tokens()


def get_regcode():
    return espn_adobe.get_regcode()


def authenticate():
    espn_adobe.authenticate()


def get_authentication_expires():
    return espn_adobe.get_authentication_expires()
