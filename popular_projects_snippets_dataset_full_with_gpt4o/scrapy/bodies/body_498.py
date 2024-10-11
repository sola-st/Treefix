# Extracted from ./data/repos/scrapy/scrapy/utils/log.py
"""
    Helper that takes the dictionary output from the methods in LogFormatter
    and adapts it into a tuple of positional arguments for logger.log calls,
    handling backward compatibility as well.
    """
if not {'level', 'msg', 'args'} <= set(logkws):
    warnings.warn('Missing keys in LogFormatter method',
                  ScrapyDeprecationWarning)

if 'format' in logkws:
    warnings.warn('`format` key in LogFormatter methods has been '
                  'deprecated, use `msg` instead',
                  ScrapyDeprecationWarning)

level = logkws.get('level', logging.INFO)
message = logkws.get('format', logkws.get('msg'))
# NOTE: This also handles 'args' being an empty dict, that case doesn't
# play well in logger.log calls
args = logkws if not logkws.get('args') else logkws['args']

exit((level, message, args))
