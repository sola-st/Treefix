import smtplib # pragma: no cover

cls = smtplib.SMTP # pragma: no cover
settings = type('Mock', (object,), { # pragma: no cover
    'MAIL_HOST': 'smtp.example.com', # pragma: no cover
    'MAIL_FROM': 'no-reply@example.com', # pragma: no cover
    'MAIL_USER': 'username', # pragma: no cover
    'MAIL_PASS': 'password', # pragma: no cover
    'MAIL_PORT': 587, # pragma: no cover
    'MAIL_TLS': True, # pragma: no cover
    'MAIL_SSL': False, # pragma: no cover
    'getint': lambda key: settings.__dict__[key], # pragma: no cover
    'getbool': lambda key: settings.__dict__[key] # pragma: no cover
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
