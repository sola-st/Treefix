# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH#25581
df1 = DataFrame(test)
result = df1.groupby(0).agg(Series.mode)
# Mode usually only returns 1 value, but can return a list in the case of a tie.

expected = DataFrame(constant)
expected = expected.set_index(0)

tm.assert_frame_equal(result, expected)
