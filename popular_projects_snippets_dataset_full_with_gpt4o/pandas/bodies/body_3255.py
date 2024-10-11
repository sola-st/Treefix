# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# see GH#11302
result = DataFrame([np.NaN]).astype(str)
expected = DataFrame(["nan"])

tm.assert_frame_equal(result, expected)
result = DataFrame([1.12345678901234567890]).astype(str)

val = "1.1234567890123457"
expected = DataFrame([val])
tm.assert_frame_equal(result, expected)
