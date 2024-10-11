import readline # pragma: no cover
from types import SimpleNamespace as Mock # pragma: no cover

namespace = None # pragma: no cover
banner = '' # pragma: no cover
shells = Mock() # pragma: no cover
def get_shell_embed_func(shells): return lambda namespace, banner: print("console started") # pragma: no cover
SystemExit = Exception # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/console.py
from l3.Runtime import _l_
"""Start Python console bound to the given namespace.
    Readline support and tab completion will be used on Unix, if available.
    """
if namespace is None:
    _l_(16810)

    namespace = {}
    _l_(16809)

try:
    _l_(16816)

    shell = get_shell_embed_func(shells)
    _l_(16811)
    if shell is not None:
        _l_(16813)

        shell(namespace=namespace, banner=banner)
        _l_(16812)
except SystemExit:
    _l_(16815)

    pass
    _l_(16814)
