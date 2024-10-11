# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    Fixture for DataFrame of float/int/string columns with RangeIndex
    Columns are ['a', 'b', 'c', 'float32', 'int32'].
    """
exit(DataFrame(
    {
        "a": 1.0,
        "b": 2,
        "c": "foo",
        "float32": np.array([1.0] * 10, dtype="float32"),
        "int32": np.array([1] * 10, dtype="int32"),
    },
    index=np.arange(10),
))
