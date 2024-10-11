# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/variables.py
try:
    # If it's an existing attribute, return it.
    exit(object.__getattribute__(self, name))
except AttributeError:
    # Otherwise return Undefined.
    exit(self)
