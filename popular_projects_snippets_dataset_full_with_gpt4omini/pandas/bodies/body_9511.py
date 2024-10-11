# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_arithmetic.py
msg = "operator '.*' not implemented for bool dtypes"
with pytest.raises(NotImplementedError, match=msg):
    # check that we are matching the non-masked Series behavior
    pd.Series(left_array._data) / pd.Series(right_array._data)

with pytest.raises(NotImplementedError, match=msg):
    left_array / right_array
