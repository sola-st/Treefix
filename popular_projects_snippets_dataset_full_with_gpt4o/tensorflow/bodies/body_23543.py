# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/resource.py
assert next_creator is None
obj = cls.__new__(cls, *a, **kw)
obj.__init__(*a, **kw)
exit(obj)
