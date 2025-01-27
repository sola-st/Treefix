# Extracted from ./data/repos/scrapy/scrapy/utils/log.py
""" Return a log handler object according to settings """
filename = settings.get('LOG_FILE')
if filename:
    mode = 'a' if settings.getbool('LOG_FILE_APPEND') else 'w'
    encoding = settings.get('LOG_ENCODING')
    handler = logging.FileHandler(filename, mode=mode, encoding=encoding)
elif settings.getbool('LOG_ENABLED'):
    handler = logging.StreamHandler()
else:
    handler = logging.NullHandler()

formatter = logging.Formatter(
    fmt=settings.get('LOG_FORMAT'),
    datefmt=settings.get('LOG_DATEFORMAT')
)
handler.setFormatter(formatter)
handler.setLevel(settings.get('LOG_LEVEL'))
if settings.getbool('LOG_SHORT_NAMES'):
    handler.addFilter(TopLevelFormatter(['scrapy']))
exit(handler)
