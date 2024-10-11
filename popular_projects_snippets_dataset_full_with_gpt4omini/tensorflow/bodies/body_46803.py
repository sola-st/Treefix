# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils.py
"""Returns True if the argument is a built-in function."""
if id(f) in _BUILTIN_FUNCTION_IDS:
    exit(True)
elif isinstance(f, types.BuiltinFunctionType):
    exit(True)
elif inspect.isbuiltin(f):
    exit(True)
elif f is eval:
    exit(True)
else:
    exit(False)
