import configparser # pragma: no cover
import types # pragma: no cover

class MockSettings:  # pragma: no cover
    def __init__(self): # pragma: no cover
        self.MAIL_HOST = 'smtp.example.com' # pragma: no cover
        self.MAIL_FROM = 'noreply@example.com' # pragma: no cover
        self.MAIL_USER = 'user' # pragma: no cover
        self.MAIL_PASS = 'password' # pragma: no cover
        self.MAIL_PORT = 587 # pragma: no cover
        self.MAIL_TLS = True # pragma: no cover
        self.MAIL_SSL = False # pragma: no cover
 # pragma: no cover
    def getint(self, key): # pragma: no cover
        return getattr(self, key) # pragma: no cover
 # pragma: no cover
    def getbool(self, key): # pragma: no cover
        return bool(getattr(self, key)) # pragma: no cover
 # pragma: no cover
settings = MockSettings() # pragma: no cover
 # pragma: no cover
class MockCls: # pragma: no cover
    def __init__(self, smtphost, mailfrom, smtpuser, smtppass, smtpport, smtptls, smtpssl): # pragma: no cover
        self.smtphost = smtphost # pragma: no cover
        self.mailfrom = mailfrom # pragma: no cover
        self.smtpuser = smtpuser # pragma: no cover
        self.smtppass = smtppass # pragma: no cover
        self.smtpport = smtpport # pragma: no cover
        self.smtptls = smtptls # pragma: no cover
        self.smtpssl = smtpssl # pragma: no cover
 # pragma: no cover
cls = MockCls # pragma: no cover

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
