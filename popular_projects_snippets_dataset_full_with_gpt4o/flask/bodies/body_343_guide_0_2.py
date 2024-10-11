import types # pragma: no cover

loader = types.SimpleNamespace() # pragma: no cover
mod_name = 'test_package' # pragma: no cover
cls = type(loader) # pragma: no cover
if not hasattr(loader, 'is_package'): # pragma: no cover
    type_name = type(loader).__name__ # pragma: no cover
    module_name = type(loader).__module__ # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Attempt to figure out if the given name is a package or a module.

    :param: loader: The loader that handled the name.
    :param mod_name: The name of the package or module.
    """
# Use loader.is_package if it's available.
if hasattr(loader, "is_package"):
    _l_(20870)

    aux = loader.is_package(mod_name)
    _l_(20869)
    exit(aux)

cls = type(loader)
_l_(20871)

# NamespaceLoader doesn't implement is_package, but all names it
# loads must be packages.
if cls.__module__ == "_frozen_importlib" and cls.__name__ == "NamespaceLoader":
    _l_(20873)

    aux = True
    _l_(20872)
    exit(aux)

# Otherwise we need to fail with an error that explains what went
# wrong.
raise AttributeError(
    f"'{cls.__name__}.is_package()' must be implemented for PEP 302"
    f" import hooks."
)
_l_(20874)
