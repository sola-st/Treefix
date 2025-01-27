# Extracted from ./data/repos/pandas/pandas/tests/frame/test_nonunique_indexes.py
# dup columns across dtype GH 2079/2194
vals = [[1, -1, 2.0], [2, -2, 3.0]]
rs = DataFrame(vals, columns=["A", "A", "B"])
xp = DataFrame(vals)
xp.columns = ["A", "A", "B"]
tm.assert_frame_equal(rs, xp)
