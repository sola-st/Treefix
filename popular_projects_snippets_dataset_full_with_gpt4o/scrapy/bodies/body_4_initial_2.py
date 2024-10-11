class MockSettings: # pragma: no cover
    def __getitem__(self, item): # pragma: no cover
        return self.__dict__.get(item)# pragma: no cover
 # pragma: no cover
    def getint(self, item): # pragma: no cover
        return int(self.__dict__.get(item))# pragma: no cover
 # pragma: no cover
    def getbool(self, item): # pragma: no cover
        return bool(self.__dict__.get(item)) # pragma: no cover
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

settings = MockSettings() # pragma: no cover
settings.MAIL_HOST = 'smtp.example.com' # pragma: no cover
settings.MAIL_FROM = 'example@example.com' # pragma: no cover
settings.MAIL_USER = 'user@example.com' # pragma: no cover
settings.MAIL_PASS = 'password' # pragma: no cover
settings.MAIL_PORT = '587' # pragma: no cover
settings.MAIL_TLS = 'True' # pragma: no cover
settings.MAIL_SSL = 'False' # pragma: no cover
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
_l_(19820)
exit(aux)
