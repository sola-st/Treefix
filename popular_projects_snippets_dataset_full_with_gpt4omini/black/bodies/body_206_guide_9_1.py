from typing import List, Any, Dict # pragma: no cover
import sys # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Make Click not crash on Python 3.6 with LANG=C.

    On certain misconfigured environments, Python 3 selects the ASCII encoding as the
    default which restricts paths that it can access during the lifetime of the
    application.  Click refuses to work in this scenario by raising a RuntimeError.

    In case of Black the likelihood that non-ASCII characters are going to be used in
    file paths is minimal since it's Python source code.  Moreover, this crash was
    spurious on Python 3.7 thanks to PEP 538 and PEP 540.
    """
modules: List[Any] = []
_l_(4949)
try:
    _l_(4954)

    from click import core
    _l_(4950)
except ImportError:
    _l_(4952)

    pass
    _l_(4951)
else:
    modules.append(core)
    _l_(4953)
try:
    _l_(4959)

    # Removed in Click 8.1.0 and newer; we keep this around for users who have
    # older versions installed.
    from click import _unicodefun  # type: ignore
    _l_(4955)  # type: ignore
except ImportError:
    _l_(4957)

    pass
    _l_(4956)
else:
    modules.append(_unicodefun)
    _l_(4958)

for module in modules:
    _l_(4964)

    if hasattr(module, "_verify_python3_env"):
        _l_(4961)

        module._verify_python3_env = lambda: None
        _l_(4960)
    if hasattr(module, "_verify_python_env"):
        _l_(4963)

        module._verify_python_env = lambda: None
        _l_(4962)
