import importlib # pragma: no cover
import sys # pragma: no cover
import warnings # pragma: no cover
from packaging.version import Version # pragma: no cover

name = 'non_existent_package' # pragma: no cover
extra = 'This package is required for proper functionality.' # pragma: no cover
errors = 'raise' # pragma: no cover
min_version = '1.0.0' # pragma: no cover
INSTALL_MAPPING = {} # pragma: no cover
VERSIONS = {} # pragma: no cover
def get_version(module): return '0.0.1' # pragma: no cover
def find_stack_level(): return 1 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/compat/_optional.py
from l3.Runtime import _l_
"""
    Import an optional dependency.

    By default, if a dependency is missing an ImportError with a nice
    message will be raised. If a dependency is present, but too old,
    we raise.

    Parameters
    ----------
    name : str
        The module name.
    extra : str
        Additional text to include in the ImportError message.
    errors : str {'raise', 'warn', 'ignore'}
        What to do when a dependency is not found or its version is too old.

        * raise : Raise an ImportError
        * warn : Only applicable when a module's version is to old.
          Warns that the version is too old and returns None
        * ignore: If the module is not installed, return None, otherwise,
          return the module, even if the version is too old.
          It's expected that users validate the version locally when
          using ``errors="ignore"`` (see. ``io/html.py``)
    min_version : str, default None
        Specify a minimum version that is different from the global pandas
        minimum version required.
    Returns
    -------
    maybe_module : Optional[ModuleType]
        The imported module, when found and the version is correct.
        None is returned when the package is not found and `errors`
        is False, or when the package's version is too old and `errors`
        is ``'warn'``.
    """

assert errors in {"warn", "raise", "ignore"}
_l_(10746)

package_name = INSTALL_MAPPING.get(name)
_l_(10747)
install_name = package_name if package_name is not None else name
_l_(10748)

msg = (
    f"Missing optional dependency '{install_name}'. {extra} "
    f"Use pip or conda to install {install_name}."
)
_l_(10749)
try:
    _l_(10755)

    module = importlib.import_module(name)
    _l_(10750)
except ImportError:
    _l_(10754)

    if errors == "raise":
        _l_(10752)

        raise ImportError(msg)
        _l_(10751)
    aux = None
    _l_(10753)
    exit(aux)

# Handle submodules: if we have submodule, grab parent module from sys.modules
parent = name.split(".")[0]
_l_(10756)
if parent != name:
    _l_(10760)

    install_name = parent
    _l_(10757)
    module_to_get = sys.modules[install_name]
    _l_(10758)
else:
    module_to_get = module
    _l_(10759)
minimum_version = min_version if min_version is not None else VERSIONS.get(parent)
_l_(10761)
if minimum_version:
    _l_(10770)

    version = get_version(module_to_get)
    _l_(10762)
    if version and Version(version) < Version(minimum_version):
        _l_(10769)

        msg = (
            f"Pandas requires version '{minimum_version}' or newer of '{parent}' "
            f"(version '{version}' currently installed)."
        )
        _l_(10763)
        if errors == "warn":
            _l_(10768)

            warnings.warn(
                msg,
                UserWarning,
                stacklevel=find_stack_level(),
            )
            _l_(10764)
            aux = None
            _l_(10765)
            exit(aux)
        elif errors == "raise":
            _l_(10767)

            raise ImportError(msg)
            _l_(10766)
aux = module
_l_(10771)

exit(aux)
