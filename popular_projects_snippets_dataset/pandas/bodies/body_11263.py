# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py

d = DataFrame([3, 1, 7, 6])
bins = [0, 5, 10, 15]
g = d.groupby(pd.cut(d[0], bins), observed=observed)

# TODO: should prob allow a str of Interval work as well
# IOW '(0, 5]'
result = g.get_group(pd.Interval(0, 5))
expected = DataFrame([3, 1], index=[0, 1])
tm.assert_frame_equal(result, expected)

msg = r"Interval\(10, 15, closed='right'\)"
with pytest.raises(KeyError, match=msg):
    g.get_group(pd.Interval(10, 15))
