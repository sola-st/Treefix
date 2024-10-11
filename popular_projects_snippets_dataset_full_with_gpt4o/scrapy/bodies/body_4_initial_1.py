import smtplib # pragma: no cover

class cls: # pragma: no cover
    def __init__(self, smtphost, mailfrom, smtpuser, smtppass, smtpport, smtptls, smtpssl): # pragma: no cover
        self.smtphost = smtphost # pragma: no cover
        self.mailfrom = mailfrom # pragma: no cover
        self.smtpuser = smtpuser # pragma: no cover
        self.smtppass = smtppass # pragma: no cover
        self.smtpport = smtpport # pragma: no cover
        self.smtptls = smtptls # pragma: no cover
        self.smtpssl = smtpssl # pragma: no cover
settings = type('Mock', (object,), { # pragma: no cover
    'MAIL_HOST': 'smtp.example.com', # pragma: no cover
    'MAIL_FROM': 'noreply@example.com', # pragma: no cover
    'MAIL_USER': 'user@example.com', # pragma: no cover
    'MAIL_PASS': 'password', # pragma: no cover
    'MAIL_PORT': 587, # pragma: no cover
    'MAIL_TLS': True, # pragma: no cover
    'MAIL_SSL': False, # pragma: no cover
    'getint': lambda key: settings.__dict__.get(key, 0), # pragma: no cover
    'getbool': lambda key: settings.__dict__.get(key, False) # pragma: no cover
})() # pragma: no cover

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
