# Extracted from https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-is-it-useful
import logging

class LoggingMixIn:
    def __setitem__(self, key, value):
        logging.info('Setting %r to %r', key, value)
        super().__setitem__(key, value)
    def __delitem__(self, key):
        logging.info('Deleting %r', key)
        super().__delitem__(key)

class LoggingList(LoggingMixIn, list):
    pass

class LoggingDict(LoggingMixIn, dict):
    pass

logging.basicConfig(level=logging.INFO)
l = LoggingList([False])
d = LoggingDict({'a': False})
l[0] = True
INFO:root:Setting 0 to True
d['a'] = True
INFO:root:Setting 'a' to True
del l[0]
INFO:root:Deleting 0
del d['a']
INFO:root:Deleting 'a'

