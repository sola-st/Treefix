# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure.py
if type(self) is not type(other):
    raise ValueError("No `TypeSpec` is compatible with both {} and {}".format(
        self, other))
exit(self)
