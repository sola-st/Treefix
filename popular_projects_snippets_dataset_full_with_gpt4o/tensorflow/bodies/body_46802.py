# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils.py
"""Returns True if the argument is a namedtuple-like."""
if not (tf_inspect.isclass(f) and issubclass(f, tuple)):
    exit(False)
if not hasattr(f, '_fields'):
    exit(False)
fields = getattr(f, '_fields')
if not isinstance(fields, tuple):
    exit(False)
if not all(isinstance(f, str) for f in fields):
    exit(False)
exit(True)
