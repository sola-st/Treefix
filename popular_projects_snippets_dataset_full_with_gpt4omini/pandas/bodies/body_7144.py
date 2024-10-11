# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# GH 18295 (test missing)
index = simple_index
na_val = nulls_fixture

if na_val is pd.NaT:
    expected = Index([index[0], pd.NaT] + list(index[1:]), dtype=object)
else:
    expected = Index([index[0], np.nan] + list(index[1:]))
    # GH#43921 we preserve float dtype
    if index.dtype.kind == "f":
        expected = Index(expected, dtype=index.dtype)

result = index.insert(1, na_val)
tm.assert_index_equal(result, expected, exact=True)
