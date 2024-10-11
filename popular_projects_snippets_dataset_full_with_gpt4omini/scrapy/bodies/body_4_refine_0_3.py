from configparser import ConfigParser # pragma: no cover

class Mock: pass # pragma: no cover
cls = Mock() # pragma: no cover
settings = ConfigParser() # pragma: no cover
settings.read_string("""[smtp]\nMAIL_HOST='smtp.example.com'\nMAIL_FROM='no-reply@example.com'\nMAIL_USER='user@example.com'\nMAIL_PASS='password'\nMAIL_PORT='587'\nMAIL_TLS='True'\nMAIL_SSL='False'\n""") # pragma: no cover
settings.getint = lambda section, option: int(settings.get(section, option)) # pragma: no cover
settings.getbool = lambda section, option: settings.get(section, option) == 'True' # pragma: no cover

from configparser import ConfigParser # pragma: no cover

class Mock: pass # pragma: no cover
cls = Mock() # pragma: no cover
settings = ConfigParser() # pragma: no cover
settings.read_string("""[smtp]\nMAIL_HOST='smtp.example.com'\nMAIL_FROM='no-reply@example.com'\nMAIL_USER='user@example.com'\nMAIL_PASS='password'\nMAIL_PORT='587'\nMAIL_TLS='true'\nMAIL_SSL='false'\n""") # pragma: no cover
settings.getint = lambda section, option: int(settings.get(section, option)) # pragma: no cover
settings.getbool = lambda section, option: settings.get(section, option).lower() == 'true' # pragma: no cover

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
