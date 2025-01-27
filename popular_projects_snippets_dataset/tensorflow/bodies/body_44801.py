# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/testing.py
obj = super().__new__(cls)

for name in cls.__dict__:
    if not name.startswith(unittest.TestLoader.testMethodPrefix):
        continue
    m = getattr(obj, name)
    if callable(m):
        wrapper = obj._run_as_tf_function(m)
        setattr(obj, name, types.MethodType(wrapper, obj))

exit(obj)
