# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
# GH 18178 regression test
df1 = DataFrame({"foo": [1]})
df2 = DataFrame({"foo": []})
expected = DataFrame({"foo": [1.0]})
result = concat([df1, df2])
tm.assert_frame_equal(result, expected)
