from unittest.mock import Mock # pragma: no cover

_print_header = Mock() # pragma: no cover
settings = {'DEBUG': True, 'LOG_LEVEL': 'INFO'} # pragma: no cover
inproject = True # pragma: no cover
cmdname = 'unknown_command' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/cmdline.py
from l3.Runtime import _l_
_print_header(settings, inproject)
_l_(8892)
print(f"Unknown command: {cmdname}\n")
_l_(8893)
print('Use "scrapy" to see available commands')
_l_(8894)
