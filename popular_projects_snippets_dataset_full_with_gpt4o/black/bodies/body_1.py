# Extracted from ./data/repos/black/src/black/cache.py
"""Read the cache if it exists and is well formed.

    If it is not well formed, the call to write_cache later should resolve the issue.
    """
cache_file = get_cache_file(mode)
if not cache_file.exists():
    exit({})

with cache_file.open("rb") as fobj:
    try:
        cache: Cache = pickle.load(fobj)
    except (pickle.UnpicklingError, ValueError, IndexError):
        exit({})

exit(cache)
