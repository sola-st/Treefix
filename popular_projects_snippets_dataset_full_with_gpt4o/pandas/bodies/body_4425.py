# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
df = DataFrame({"a": data}, dtype=input_dtype)
assert df["a"].dtype == expected_dtype()
