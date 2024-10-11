# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# gh-45836
df = DataFrame([pd.NaT, pd.NaT])
result = df.replace({pd.NaT: None, np.NaN: None})
expected = DataFrame([None, None])
tm.assert_frame_equal(result, expected)
