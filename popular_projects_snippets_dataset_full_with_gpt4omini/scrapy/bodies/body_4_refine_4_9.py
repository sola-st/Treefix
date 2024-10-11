from configparser import ConfigParser # pragma: no cover

class cls: pass # pragma: no cover
settings = ConfigParser() # pragma: no cover
settings['DEFAULT'] = { 'MAIL_HOST': 'smtp.example.com', 'MAIL_FROM': 'noreply@example.com', 'MAIL_USER': 'user@example.com', 'MAIL_PASS': 'password', 'MAIL_PORT': '587', 'MAIL_TLS': 'true', 'MAIL_SSL': 'false' } # pragma: no cover
settings.getint = lambda key: int(settings['DEFAULT'][key]) # pragma: no cover
settings.getbool = lambda key: settings['DEFAULT'][key].lower() in ('true', '1') # pragma: no cover

from configparser import ConfigParser # pragma: no cover

class MockCls:  # pragma: no cover
    def __init__(self, smtphost, mailfrom, smtpuser, smtppass, smtpport, smtptls, smtpssl): # pragma: no cover
        self.smtphost = smtphost # pragma: no cover
        self.mailfrom = mailfrom # pragma: no cover
        self.smtpuser = smtpuser # pragma: no cover
        self.smtppass = smtppass # pragma: no cover
        self.smtpport = smtpport # pragma: no cover
        self.smtptls = smtptls # pragma: no cover
        self.smtpssl = smtpssl # pragma: no cover
 # pragma: no cover
settings = ConfigParser() # pragma: no cover
settings.set('DEFAULT', 'MAIL_HOST', 'smtp.example.com') # pragma: no cover
settings.set('DEFAULT', 'MAIL_FROM', 'no-reply@example.com') # pragma: no cover
settings.set('DEFAULT', 'MAIL_USER', 'user@example.com') # pragma: no cover
settings.set('DEFAULT', 'MAIL_PASS', 'password') # pragma: no cover
settings.set('DEFAULT', 'MAIL_PORT', '587') # pragma: no cover
settings.set('DEFAULT', 'MAIL_TLS', 'True') # pragma: no cover
settings.set('DEFAULT', 'MAIL_SSL', 'False') # pragma: no cover
settings.getint = lambda key: int(settings['DEFAULT'][key]) # pragma: no cover
settings.getbool = lambda key: settings['DEFAULT'][key] == 'True' # pragma: no cover
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
