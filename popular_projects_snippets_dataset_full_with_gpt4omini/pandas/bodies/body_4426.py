# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
data = {"int": 1, "bool": True, "float": 3.0, "complex": 4j, "object": "foo"}
df = DataFrame(data, index=np.arange(10))

assert df["int"].dtype == np.int64
assert df["bool"].dtype == np.bool_
assert df["float"].dtype == np.float64
assert df["complex"].dtype == np.complex128
assert df["object"].dtype == np.object_
