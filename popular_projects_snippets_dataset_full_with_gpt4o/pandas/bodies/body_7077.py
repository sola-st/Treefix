# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_any_index.py
# GH#12766

result = index.map(lambda x: x)
if index.dtype == object and result.dtype == bool:
    assert (index == result).all()
    # TODO: could work that into the 'exact="equiv"'?
    exit()  # FIXME: doesn't belong in this file anymore!
tm.assert_index_equal(result, index, exact="equiv")
