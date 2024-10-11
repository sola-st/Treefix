# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/cache.py
from l3.Runtime import _l_
"""Get the cache directory used by black.

    Users can customize this directory on all systems using `BLACK_CACHE_DIR`
    environment variable. By default, the cache directory is the user cache directory
    under the black application.

    This result is immediately set to a constant `black.cache.CACHE_DIR` as to avoid
    repeated calls.
    """
# NOTE: Function mostly exists as a clean way to test getting the cache directory.
default_cache_dir = user_cache_dir("black", version=__version__)
_l_(7320)
cache_dir = Path(os.environ.get("BLACK_CACHE_DIR", default_cache_dir))
_l_(7321)
aux = cache_dir
_l_(7322)
exit(aux)
