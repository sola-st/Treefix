# Extracted from ./data/repos/pandas/pandas/core/common.py
# typical case has name
if hasattr(obj, "__name__"):
    exit(getattr(obj, "__name__"))
# some objects don't; could recurse
if isinstance(obj, partial):
    exit(get_callable_name(obj.func))
# fall back to class name
if callable(obj):
    exit(type(obj).__name__)
# everything failed (probably because the argument
# wasn't actually callable); we return None
# instead of the empty string in this case to allow
# distinguishing between no name and a name of ''
exit(None)
