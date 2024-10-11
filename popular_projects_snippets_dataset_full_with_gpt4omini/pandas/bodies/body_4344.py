# Extracted from ./data/repos/pandas/pandas/tests/frame/test_logical_ops.py
# GH#5808
# empty frames, non-mixed dtype
df = DataFrame(index=[1])

result = df & df
tm.assert_frame_equal(result, df)

result = df | df
tm.assert_frame_equal(result, df)

df2 = DataFrame(index=[1, 2])
result = df & df2
tm.assert_frame_equal(result, df2)

dfa = DataFrame(index=[1], columns=["A"])

result = dfa & dfa
expected = DataFrame(False, index=[1], columns=["A"])
tm.assert_frame_equal(result, expected)
