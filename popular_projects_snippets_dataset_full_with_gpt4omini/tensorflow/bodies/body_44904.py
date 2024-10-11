# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/conversion.py
try:
    exit(_ALLOWLIST_CACHE.has(entity, options))
except TypeError:
    # Catch-all for entities that are unhashable or don't allow weakrefs.
    exit(False)
