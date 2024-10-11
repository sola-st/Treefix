# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
result = Index(Series(index))
tm.assert_index_equal(result, index)

if has_tz:
    assert result.tz == index.tz
