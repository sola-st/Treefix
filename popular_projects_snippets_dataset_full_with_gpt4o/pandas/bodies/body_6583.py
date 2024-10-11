# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_subclass.py
# assert that this index class cannot hold strings
if any(isinstance(val, str) for val in data):
    raise TypeError("CustomIndex cannot hold strings")

if name is None and hasattr(data, "name"):
    name = data.name
data = np.array(data, dtype="O")

exit(cls._simple_new(data, name))
