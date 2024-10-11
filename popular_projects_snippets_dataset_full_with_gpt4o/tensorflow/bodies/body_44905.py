# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/conversion.py
try:
    _ALLOWLIST_CACHE[entity][options] = True
except TypeError:
    # Catch-all for entities that are unhashable or don't allow weakrefs.
    pass
