import types # pragma: no cover

self = types.SimpleNamespace() # pragma: no cover
self.long_desc = lambda: 'This is a long description that provides extensive help for the command.' # pragma: no cover

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
