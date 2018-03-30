
# For the Dev VM environment, we use the same settings as the
# sample prod_settings.py file, with a few exceptions.
from .prod_settings_template import *
import os
import pwd
from typing import Set

LOCAL_UPLOADS_DIR = 'var/uploads'
EMAIL_LOG_DIR = "/var/log/zulip/email.log"
FORWARD_ADDRESS_CONFIG_FILE = "var/forward_address.ini"
# Check if test_settings.py set EXTERNAL_HOST.
EXTERNAL_HOST = os.getenv('EXTERNAL_HOST')
if EXTERNAL_HOST is None:
    user_id = os.getuid()
    user_name = pwd.getpwuid(user_id).pw_name
    if user_name == "zulipdev":
        # For our droplets, we use the external hostname by default.
        EXTERNAL_HOST = os.uname()[1].lower() + ":9991"
    else:
        # For local development environments, we use localhost by
        # default, via the "zulipdev.com" hostname.
        EXTERNAL_HOST = 'zulipdev.com:9991'
        # Serve the main dev realm at the literal name "localhost",
        # so it works out of the box even when not on the Internet.
        REALM_HOSTS = {
            'zulip': 'localhost:9991'
        }
else:
    REALM_HOSTS = {
        'zulip': EXTERNAL_HOST,
    }

ALLOWED_HOSTS = ['*']

# Uncomment extra backends if you want to test with them.  Note that
# for Google and GitHub auth you'll need to do some pre-setup.
AUTHENTICATION_BACKENDS = (
    'zproject.backends.DevAuthBackend',
    'zproject.backends.EmailAuthBackend',
    'zproject.backends.GitHubAuthBackend',
    'zproject.backends.GoogleMobileOauth2Backend',
    'zproject.backends.SAMLAuthBackend'
)

EXTERNAL_URI_SCHEME = "http://"
EMAIL_GATEWAY_PATTERN = "%s@" + EXTERNAL_HOST
NOTIFICATION_BOT = "notification-bot@zulip.com"
ERROR_BOT = "error-bot@zulip.com"
EMAIL_GATEWAY_BOT = "emailgateway@zulip.com"
PHYSICAL_ADDRESS = "Zulip Headquarters, 123 Octo Stream, South Pacific Ocean"
EXTRA_INSTALLED_APPS = ["zilencer", "analytics"]
# Disable Camo in development
CAMO_URI = ''

OPEN_REALM_CREATION = True
INVITES_MIN_USER_AGE_DAYS = 0

EMBEDDED_BOTS_ENABLED = True

SAVE_FRONTEND_STACKTRACES = True
EVENT_LOGS_ENABLED = True
STAGING_ERROR_NOTIFICATIONS = True

SYSTEM_ONLY_REALMS = set()  # type: Set[str]
USING_PGROONGA = True
# Flush cache after migration.
POST_MIGRATION_CACHE_FLUSHING = True  # type: bool

# Enable inline open graph preview in development for now
INLINE_URL_EMBED_PREVIEW = True

# Don't require anything about password strength in development
PASSWORD_MIN_LENGTH = 0
PASSWORD_MIN_GUESSES = 0

# SMTP settings for forwarding emails sent in development
# environment to an email account.
EMAIL_HOST = ""
EMAIL_HOST_USER = ""

# Two factor authentication: Use the fake backend for development.
TWO_FACTOR_CALL_GATEWAY = 'two_factor.gateways.fake.Fake'
TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.fake.Fake'

# Make sendfile use django to serve files in development
SENDFILE_BACKEND = 'sendfile.backends.development'

# Set this True to send all hotspots in development
ALWAYS_SEND_ALL_HOTSPOTS = False  # type: bool

SOCIAL_AUTH_SAML_SP_ENTITY_ID = "http://zulip.kao.cat:9991"
SOCIAL_AUTH_SAML_SP_PUBLIC_CERT =   "MIIDXTCCAkWgAwIBAgIJAN+ZB1GLy1WrMA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNV"\
                                    "BAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEwHwYDVQQKDBhJbnRlcm5ldCBX"\
                                    "aWRnaXRzIFB0eSBMdGQwHhcNMTgwMzIzMTQzMTA5WhcNMjgwMzIyMTQzMTA5WjBF"\
                                    "MQswCQYDVQQGEwJBVTETMBEGA1UECAwKU29tZS1TdGF0ZTEhMB8GA1UECgwYSW50"\
                                    "ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB"\
                                    "CgKCAQEArPZDoI+v6qaWTblIO7mXf1I/gra4WU8oiMQQdekHaSiwuB9YaXPhQRK2"\
                                    "nNozF9z8Igk/v/LFkafIThHKghxj5k6RJ+Gk8scvkGAgiKgZZ71QUPfXqL2BiI33"\
                                    "cViQaGZWwNgBFVjWNdY7dPa32ERjcCkH+jQwzVZrBOoqHQyXqLwyrwimoC8WeWjV"\
                                    "MdYp/UhIJbCPDFmDGEvf1Mocq9RNIPadq0iVUJLab0xzEXC/UJiUSYcCvzr9NYfh"\
                                    "D7F7Kfd45pfw5wf+DCYFTkvN0BfoyVaEeMccs/MyMVyvgpLw9BHt/ULEH0mHiwhc"\
                                    "VjuVxiMBegZmjLq0slfRnkIdn/Z2LQIDAQABo1AwTjAdBgNVHQ4EFgQU6Hp8D9jY"\
                                    "VSusqD9maOv7rL4UJ38wHwYDVR0jBBgwFoAU6Hp8D9jYVSusqD9maOv7rL4UJ38w"\
                                    "DAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEAlRYlhgwwE+jhj/Zyk6YA"\
                                    "XnnaQKpfcCMYLb2DyD9h/tKHPoeCWhYgul+6N4dSi1RV/F3sLBvz34EbrsUFtbfQ"\
                                    "1LJJMCIxzdcRDpn6QLXhW0QTnpeTOwFzQ3tubfIStAJELGKpk2Kjg2Q0iWzYveqI"\
                                    "t2CB1ibYiOoQ4SFXlobVTc9+5+zWLcqti1Yg0mq+b9BEpNG95ne8rE+NYvAjcjC+"\
                                    "bFfUtWYcLRU6AkYhi93EnI+SQKVUDAi9QMwzecMAcluYeJtW0cplLVgC/fE0kV/g"\
                                    "QfupXEjz6noHsAwFWXRX3e7CNHP65Fd2fNxOcMZf7B1nFhjMf2TPFav6Ci+cFUXi"\
                                    "Jg=="

SOCIAL_AUTH_SAML_ORG_INFO = {
    "en-US": {
        "name": "Zulip dev",
        "displayname": "nyan-salmon",
        "url": "http://zulip.kao.cat:9991",
    }
}
SOCIAL_AUTH_SAML_TECHNICAL_CONTACT = {
    "givenName": "nyan-salmon",
    "emailAddress": "nyan.salmon+dev@gmail.com"
}
SOCIAL_AUTH_SAML_SUPPORT_CONTACT = {
    "givenName": "nyan-salmon",
    "emailAddress": "nyan.salmon+dev@gmail.com",
}
SOCIAL_AUTH_SAML_ENABLED_IDPS = {
    "testshib": {
        "entity_id": "https://idp.testshib.org/idp/shibboleth",
        "url": "https://idp.testshib.org/idp/profile/SAML2/Redirect/SSO",
        "x509cert": "MIIDAzCCAeugAwIBAgIVAPX0G6LuoXnKS0Muei006mVSBXbvMA0GCSqGSIb3DQEB"
                    "CwUAMBsxGTAXBgNVBAMMEGlkcC50ZXN0c2hpYi5vcmcwHhcNMTYwODIzMjEyMDU0"
                    "WhcNMzYwODIzMjEyMDU0WjAbMRkwFwYDVQQDDBBpZHAudGVzdHNoaWIub3JnMIIB"
                    "IjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAg9C4J2DiRTEhJAWzPt1S3ryh"
                    "m3M2P3hPpwJwvt2q948vdTUxhhvNMuc3M3S4WNh6JYBs53R+YmjqJAII4ShMGNEm"
                    "lGnSVfHorex7IxikpuDPKV3SNf28mCAZbQrX+hWA+ann/uifVzqXktOjs6DdzdBn"
                    "xoVhniXgC8WCJwKcx6JO/hHsH1rG/0DSDeZFpTTcZHj4S9MlLNUtt5JxRzV/MmmB"
                    "3ObaX0CMqsSWUOQeE4nylSlp5RWHCnx70cs9kwz5WrflnbnzCeHU2sdbNotBEeTH"
                    "ot6a2cj/pXlRJIgPsrL/4VSicPZcGYMJMPoLTJ8mdy6mpR6nbCmP7dVbCIm/DQID"
                    "AQABoz4wPDAdBgNVHQ4EFgQUUfaDa2mPi24x09yWp1OFXmZ2GPswGwYDVR0RBBQw"
                    "EoIQaWRwLnRlc3RzaGliLm9yZzANBgkqhkiG9w0BAQsFAAOCAQEASKKgqTxhqBzR"
                    "OZ1eVy++si+eTTUQZU4+8UywSKLia2RattaAPMAcXUjO+3cYOQXLVASdlJtt+8QP"
                    "dRkfp8SiJemHPXC8BES83pogJPYEGJsKo19l4XFJHPnPy+Dsn3mlJyOfAa8RyWBS"
                    "80u5lrvAcr2TJXt9fXgkYs7BOCigxtZoR8flceGRlAZ4p5FPPxQR6NDYb645jtOT"
                    "MVr3zgfjP6Wh2dt+2p04LG7ENJn8/gEwtXVuXCsPoSCDx9Y0QmyXTJNdV1aB0AhO"
                    "RkWPlFYwp+zOyOIR+3m1+pqWFpn0eT/HrxpdKa74FA3R2kq4R7dXe4G0kUgXTdqX",
    }
}