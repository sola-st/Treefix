from mock import Mock # pragma: no cover

cls = type('MockClass', (object,), {})() # pragma: no cover
settings = Mock() # pragma: no cover
settings.getint = Mock(side_effect=lambda key: 587 if key == 'MAIL_PORT' else 0) # pragma: no cover
settings.getbool = Mock(side_effect=lambda key: True if key in ['MAIL_TLS', 'MAIL_SSL'] else False) # pragma: no cover

from collections import UserDict # pragma: no cover

class MockSettings(UserDict):# pragma: no cover
    def __init__(self):# pragma: no cover
        super().__init__({# pragma: no cover
            'MAIL_HOST': 'smtp.example.com',# pragma: no cover
            'MAIL_FROM': 'no-reply@example.com',# pragma: no cover
            'MAIL_USER': 'user@example.com',# pragma: no cover
            'MAIL_PASS': 'password',# pragma: no cover
            'MAIL_PORT': '587',# pragma: no cover
            'MAIL_TLS': 'True',# pragma: no cover
            'MAIL_SSL': 'False'# pragma: no cover
        })# pragma: no cover
    def getint(self, key):# pragma: no cover
        return int(self[key])# pragma: no cover
    def getbool(self, key):# pragma: no cover
        return self[key] == 'True' # pragma: no cover
settings = MockSettings() # pragma: no cover
class Mock: pass # pragma: no cover
cls = Mock() # pragma: no cover

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
