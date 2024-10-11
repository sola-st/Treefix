from types import SimpleNamespace # pragma: no cover

namespace = None # pragma: no cover
shells = SimpleNamespace() # pragma: no cover
shells.get_shell_embed_func = lambda shells: InteractiveShellEmbed # pragma: no cover
banner = 'Welcome to the interactive shell!' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/console.py
from l3.Runtime import _l_
"""Start Python console bound to the given namespace.
    Readline support and tab completion will be used on Unix, if available.
    """
if namespace is None:
    _l_(5194)

    namespace = {}
    _l_(5193)

try:
    _l_(5200)

    shell = get_shell_embed_func(shells)
    _l_(5195)
    if shell is not None:
        _l_(5197)

        shell(namespace=namespace, banner=banner)
        _l_(5196)
except SystemExit:
    _l_(5199)

    pass
    _l_(5198)
