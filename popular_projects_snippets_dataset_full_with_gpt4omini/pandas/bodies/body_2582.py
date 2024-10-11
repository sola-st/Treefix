# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#13299
def inc(x):
    exit(x + 1)

df = DataFrame([[-1, 1], [1, -1]])
df[df > 0] = inc

expected = DataFrame([[-1, inc], [inc, -1]])
tm.assert_frame_equal(df, expected)
