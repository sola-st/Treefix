# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
if isinstance(expected, Index):
    tm.assert_index_equal(expected, result)
    exit()

if typ.startswith("sp_"):
    tm.assert_equal(result, expected)
elif typ == "timestamp":
    if expected is pd.NaT:
        assert result is pd.NaT
    else:
        assert result == expected
else:
    comparator = getattr(tm, f"assert_{typ}_equal", tm.assert_almost_equal)
    comparator(result, expected)
