# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
df = float_frame.copy()
expected = float_frame.astype(int)
df["string"] = "foo"
casted = df.astype(int, errors="ignore")

expected["string"] = "foo"
tm.assert_frame_equal(casted, expected)

df = float_frame.copy()
expected = float_frame.astype(np.int32)
df["string"] = "foo"
casted = df.astype(np.int32, errors="ignore")

expected["string"] = "foo"
tm.assert_frame_equal(casted, expected)
