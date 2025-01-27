# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
df = simple_frame

row = df.xs("a")
col = df["two"]
# special case for some reason
tm.assert_frame_equal(df.add(row, axis=None), df + row)

# cases which will be refactored after big arithmetic refactor
tm.assert_frame_equal(df.div(row), df / row)
tm.assert_frame_equal(df.div(col, axis=0), (df.T / col).T)
