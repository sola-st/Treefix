import types # pragma: no cover

self = type('Mock', (object,), {'long_desc': lambda: 'An extensive help for the command. It will be shown when using the help command. It can contain newlines since no post-formatting will be applied to its contents.'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/commands/__init__.py
from l3.Runtime import _l_
"""An extensive help for the command. It will be shown when using the
        "help" command. It can contain newlines since no post-formatting will
        be applied to its contents.
        """
aux = self.long_desc()
_l_(7515)
exit(aux)
