from configparser import ConfigParser # pragma: no cover

class MockSettings:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.settings = {# pragma: no cover
            'MAIL_HOST': 'smtp.example.com',# pragma: no cover
            'MAIL_FROM': 'noreply@example.com',# pragma: no cover
            'MAIL_USER': 'user@example.com',# pragma: no cover
            'MAIL_PASS': 'password',# pragma: no cover
            'MAIL_PORT': '587',# pragma: no cover
            'MAIL_TLS': 'true',# pragma: no cover
            'MAIL_SSL': 'false'# pragma: no cover
        }# pragma: no cover
# pragma: no cover
    def getint(self, key):# pragma: no cover
        return int(self.settings[key])# pragma: no cover
# pragma: no cover
    def getbool(self, key):# pragma: no cover
        value = self.settings[key].lower()# pragma: no cover
        return value in ['true', '1', 'yes']# pragma: no cover
# pragma: no cover
settings = MockSettings() # pragma: no cover
cls = type('MockClass', (object,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/mail.py
from l3.Runtime import _l_
aux = cls(
    smtphost=settings['MAIL_HOST'],
    mailfrom=settings['MAIL_FROM'],
    smtpuser=settings['MAIL_USER'],
    smtppass=settings['MAIL_PASS'],
    smtpport=settings.getint('MAIL_PORT'),
    smtptls=settings.getbool('MAIL_TLS'),
    smtpssl=settings.getbool('MAIL_SSL'),
)
_l_(8836)
exit(aux)
