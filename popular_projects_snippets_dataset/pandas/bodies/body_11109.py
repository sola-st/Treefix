# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH 1313, GH 13901
s = Series([1, 2, 3, 10, 4, 5, 20, 6], Index([1, 2, 3, 1, 4, 5, 2, 6], name="foo"))
expected = Series([11, 22, 3, 4, 5, 6], Index(range(1, 7), name="foo"))

result = s.groupby(level=0).sum()
tm.assert_series_equal(result, expected)
result = s.groupby(level=[0]).sum()
tm.assert_series_equal(result, expected)
result = s.groupby(level=-1).sum()
tm.assert_series_equal(result, expected)
result = s.groupby(level=[-1]).sum()
tm.assert_series_equal(result, expected)

msg = "level > 0 or level < -1 only valid with MultiIndex"
with pytest.raises(ValueError, match=msg):
    s.groupby(level=1)
with pytest.raises(ValueError, match=msg):
    s.groupby(level=-2)
msg = "No group keys passed!"
with pytest.raises(ValueError, match=msg):
    s.groupby(level=[])
msg = "multiple levels only valid with MultiIndex"
with pytest.raises(ValueError, match=msg):
    s.groupby(level=[0, 0])
with pytest.raises(ValueError, match=msg):
    s.groupby(level=[0, 1])
msg = "level > 0 or level < -1 only valid with MultiIndex"
with pytest.raises(ValueError, match=msg):
    s.groupby(level=[1])
