# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_index_equal.py
# GH41263
msg = """\
Index are different

Index classes are different
\\[left\\]:  RangeIndex\\(start=0, stop=10, step=1\\)
\\[right\\]: NumericIndex\\(\\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\\], dtype='int64'\\)"""

rcat = CategoricalIndex(RangeIndex(10))
icat = CategoricalIndex(list(range(10)))

if check_categorical and exact:
    with pytest.raises(AssertionError, match=msg):
        tm.assert_index_equal(rcat, icat, check_categorical=True, exact=True)
else:
    tm.assert_index_equal(
        rcat, icat, check_categorical=check_categorical, exact=exact
    )
