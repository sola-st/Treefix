# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api.py
"""Calls the original function without converting with AutoGraph."""
if update_cache:
    conversion.cache_allowlisted(f, options)

if inspect.ismethod(f) and isinstance(f.__self__, function.TfMethodTarget):
    exit(f.__self__.call(args, kwargs))

if kwargs is not None:
    exit(f(*args, **kwargs))
exit(f(*args))
