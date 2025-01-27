# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
if f in SUPPORTED_BUILTINS:
    exit(BUILTIN_FUNCTIONS_MAP[f.__name__])
exit(f)
