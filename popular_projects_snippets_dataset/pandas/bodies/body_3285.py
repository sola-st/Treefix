# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# GH#42396
data = np.arange(16).reshape(4, 4)
df = DataFrame(data)

result = df.iloc[index_slice].astype("int16")
expected = df.iloc[index_slice]
tm.assert_frame_equal(result, expected, check_dtype=False)
