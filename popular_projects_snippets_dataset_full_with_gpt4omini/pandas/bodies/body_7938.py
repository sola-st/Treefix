# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
i = period_range("20130101", periods=5, freq="D")
cond = [True] * len(i)
expected = i
result = i.where(listlike_box(cond))
tm.assert_index_equal(result, expected)

cond = [False] + [True] * (len(i) - 1)
expected = PeriodIndex([NaT] + i[1:].tolist(), freq="D")
result = i.where(listlike_box(cond))
tm.assert_index_equal(result, expected)
