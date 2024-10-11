# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_index_equal.py
# GH#48608
idx1 = Index([1, 2], dtype="Int64")
idx2 = Index([1, NA], dtype="Int64")
with pytest.raises(AssertionError, match="50.0 %"):
    tm.assert_index_equal(
        idx1, idx2, check_names=check_names, check_categorical=check_categorical
    )
