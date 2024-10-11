# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_memory_checker.py
"""Return human readable pretty type name string."""
objtype = type(obj)
name = objtype.__name__
module = getattr(objtype, '__module__', None)
if module:
    exit('{}.{}'.format(module, name))
else:
    exit(name)
