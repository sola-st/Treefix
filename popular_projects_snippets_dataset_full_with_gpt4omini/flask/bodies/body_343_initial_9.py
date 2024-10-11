import types # pragma: no cover
import _frozen_importlib # pragma: no cover

class MockLoader:# pragma: no cover
    def is_package(self, name):# pragma: no cover
        return True  # Assuming the mock loader treats everything as a package# pragma: no cover
# pragma: no cover
loader = MockLoader() # pragma: no cover
mod_name = 'example_package' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Attempt to figure out if the given name is a package or a module.

    :param: loader: The loader that handled the name.
    :param mod_name: The name of the package or module.
    """
# Use loader.is_package if it's available.
if hasattr(loader, "is_package"):
    _l_(9622)

    aux = loader.is_package(mod_name)
    _l_(9621)
    exit(aux)

cls = type(loader)
_l_(9623)

# NamespaceLoader doesn't implement is_package, but all names it
# loads must be packages.
if cls.__module__ == "_frozen_importlib" and cls.__name__ == "NamespaceLoader":
    _l_(9625)

    aux = True
    _l_(9624)
    exit(aux)

# Otherwise we need to fail with an error that explains what went
# wrong.
raise AttributeError(
    f"'{cls.__name__}.is_package()' must be implemented for PEP 302"
    f" import hooks."
)
_l_(9626)
