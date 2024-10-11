from unittest.mock import Mock # pragma: no cover

cls = type('MockClass', (object,), {}) # pragma: no cover
settings = Mock() # pragma: no cover
settings.getint = Mock(return_value=587) # pragma: no cover
settings.getbool = Mock(side_effect=lambda key: { 'MAIL_TLS': True, 'MAIL_SSL': False }[key]) # pragma: no cover

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
