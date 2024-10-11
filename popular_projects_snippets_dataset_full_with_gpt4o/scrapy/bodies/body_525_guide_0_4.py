import sys # pragma: no cover
from types import SimpleNamespace # pragma: no cover

namespace = None # pragma: no cover
banner = 'Welcome to the custom Python shell!' # pragma: no cover
class MockShell: # pragma: no cover
    def __call__(self, namespace, banner): # pragma: no cover
        print(banner) # pragma: no cover
def get_shell_embed_func(shells): # pragma: no cover
    return MockShell() # pragma: no cover
shells = SimpleNamespace() # pragma: no cover

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
