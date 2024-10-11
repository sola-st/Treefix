# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
# GH 39426
values = list(range(21))
expected = DataFrame([values], columns=values)
df = expected.sort_values(expected.index[0], axis=1, ignore_index=True)

tm.assert_frame_equal(df, expected)
