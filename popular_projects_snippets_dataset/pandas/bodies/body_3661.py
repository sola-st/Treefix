# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename.py
# GH 13473
# rename now works with errors parameter
df = DataFrame(columns=["A", "B", "C", "D"])
result = df.rename(columns=mapper, errors=errors)
expected = DataFrame(columns=expected_columns)
tm.assert_frame_equal(result, expected)
