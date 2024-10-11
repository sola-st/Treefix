# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_object.py
result = object.__new__(cls)
result._data = values
result._name = name
result._calls = 0
result._reset_identity()

exit(result)
