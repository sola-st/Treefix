# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_convert_dtypes.py
# GH-43183
byte_str = b"binary-string"

df = pd.DataFrame(data={"A": byte_str}, index=[0])
result = df.convert_dtypes()
expected = df
tm.assert_frame_equal(result, expected)
