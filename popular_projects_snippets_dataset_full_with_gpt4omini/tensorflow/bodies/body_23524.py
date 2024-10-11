# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/resource_test.py
instance = next_creator(*a, **kwargs)
instance._value = 1
exit(instance)
