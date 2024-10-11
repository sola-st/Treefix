import importlib # pragma: no cover
import pathlib # pragma: no cover
import os # pragma: no cover
import pkgutil # pragma: no cover

_ = type('Mock', (object,), {})() # pragma: no cover
_._ = type('Mock', (object,), {})() # pragma: no cover
_._._ = type('Mock', (object,), {})() # pragma: no cover
_matching_loader_thinks_module_is_package = lambda loader, name: False # pragma: no cover
_path_is_relative_to = lambda path, location: True # pragma: no cover
pathlib.Path = type('Mock', (object,), {'cwd': lambda: '/mock_current_directory', 'commonpath': lambda paths: '/mock_common_path'}) # pragma: no cover
os.path = type('Mock', (object,), {'dirname': os.path.dirname, 'abspath': os.path.abspath}) # pragma: no cover
os.getcwd = lambda: '/mock_current_directory' # pragma: no cover
pkgutil.get_loader = lambda name: type('Mock', (object,), {'get_filename': lambda name: '/mock_loader_path/__module.py', 'archive': None})() # pragma: no cover

import importlib # pragma: no cover
import pathlib # pragma: no cover
import os # pragma: no cover
import pkgutil # pragma: no cover

_matching_loader_thinks_module_is_package = lambda loader, name: False # pragma: no cover
_path_is_relative_to = lambda package_path, location: True # pragma: no cover
pathlib.Path = type('MockPath', (object,), {'commonpath': staticmethod(lambda paths: '/common/path')}) # pragma: no cover
os.path = type('MockOsPath', (object,), {'dirname': staticmethod(lambda path: '/dirname'), 'abspath': staticmethod(lambda path: '/abs/path')}) # pragma: no cover
pkgutil.get_loader = lambda name: type('MockLoader', (object,), {'get_filename': lambda self: '/mock_loader_path/__module.py'})() # pragma: no cover
os.getcwd = lambda: '/current/working/dir' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Find the path that contains the package or module."""
root_mod_name, _, _ = import_name.partition(".")
_l_(22799)

try:
    _l_(22815)

    root_spec = importlib.util.find_spec(root_mod_name)
    _l_(22800)

    if root_spec is None:
        _l_(22802)

        raise ValueError("not found")
        _l_(22801)
except (ImportError, ValueError):
    _l_(22804)

    pass  # handled below
    _l_(22803)  # handled below
else:
    # namespace package
    if root_spec.origin in {"namespace", None}:
        _l_(22814)

        package_spec = importlib.util.find_spec(import_name)
        _l_(22805)
        if package_spec is not None and package_spec.submodule_search_locations:
            _l_(22809)

            # Pick the path in the namespace that contains the submodule.
            package_path = pathlib.Path(
                os.path.commonpath(package_spec.submodule_search_locations)
            )
            _l_(22806)
            search_locations = (
                location
                for location in root_spec.submodule_search_locations
                if _path_is_relative_to(package_path, location)
            )
            _l_(22807)
        else:
            # Pick the first path.
            search_locations = iter(root_spec.submodule_search_locations)
            _l_(22808)
        aux = os.path.dirname(next(search_locations))
        _l_(22810)
        exit(aux)
    # a package (with __init__.py)
    elif root_spec.submodule_search_locations:
        _l_(22813)

        aux = os.path.dirname(os.path.dirname(root_spec.origin))
        _l_(22811)
        exit(aux)
    # just a normal module
    else:
        aux = os.path.dirname(root_spec.origin)
        _l_(22812)
        exit(aux)

    # we were unable to find the `package_path` using PEP 451 loaders
loader = pkgutil.get_loader(root_mod_name)
_l_(22816)

if loader is None or root_mod_name == "__main__":
    _l_(22818)

    aux = os.getcwd()
    _l_(22817)
    # import name is not found, or interactive/main module
    exit(aux)

if hasattr(loader, "get_filename"):
    _l_(22823)

    filename = loader.get_filename(root_mod_name)
    _l_(22819)
elif hasattr(loader, "archive"):
    _l_(22822)

    # zipimporter's loader.archive points to the .egg or .zip file.
    filename = loader.archive
    _l_(22820)
else:
    # At least one loader is missing both get_filename and archive:
    # Google App Engine's HardenedModulesHook, use __file__.
    filename = importlib.import_module(root_mod_name).__file__
    _l_(22821)

package_path = os.path.abspath(os.path.dirname(filename))
_l_(22824)

# If the imported name is a package, filename is currently pointing
# to the root of the package, need to get the current directory.
if _matching_loader_thinks_module_is_package(loader, root_mod_name):
    _l_(22826)

    package_path = os.path.dirname(package_path)
    _l_(22825)
aux = package_path
_l_(22827)

exit(aux)
