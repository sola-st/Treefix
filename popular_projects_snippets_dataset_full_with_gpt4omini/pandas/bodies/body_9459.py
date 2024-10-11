# Extracted from ./data/repos/pandas/pandas/tests/arrays/timedeltas/test_constructors.py
with pytest.raises(ValueError, match="dtype bool cannot be converted"):
    TimedeltaArray(np.array([1, 2, 3], dtype="bool"))
