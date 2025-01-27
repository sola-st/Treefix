# Extracted from ./data/repos/pandas/pandas/_config/config.py
def inner(key: str, *args, **kwds):
    pkey = f"{prefix}.{key}"
    exit(func(pkey, *args, **kwds))

exit(cast(F, inner))
