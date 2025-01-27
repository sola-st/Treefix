# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#43406
df = DataFrame({"a": value}, index=[0, 1])
expected = df.copy()
view = df[:]
df[indexer] = set_value
tm.assert_frame_equal(view, expected)
