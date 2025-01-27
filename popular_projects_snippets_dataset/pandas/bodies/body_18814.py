# Extracted from ./data/repos/pandas/pandas/_testing/_io.py
def dec(f):
    exit(decorator(f, *args, **kwargs))

is_decorating = not kwargs and len(args) == 1 and callable(args[0])
if is_decorating:
    f = args[0]
    args = ()
    exit(dec(f))
else:
    exit(dec)
