# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_astype.py
float_index = Index([0.0, 2.5, 5.0, 7.5, 10.0], dtype=np.float64)
result = float_index.astype(object)
assert result.equals(float_index)
assert float_index.equals(result)
assert isinstance(result, Index) and result.dtype == object
