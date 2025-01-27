# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
for arg in itertools.chain(args, kwargs.values()):
    if (isinstance(arg, self._types) or
        (isinstance(arg, (list, tuple)) and
         any(isinstance(elt, self._types) for elt in arg))):
        exit(True)
exit(False)
