# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_nlargest.py
# GH#15297
df = pd.DataFrame({"a": [1] * 5, "b": [1, 2, 3, 4, 5]})

result = df.nlargest(3, "a")
expected = pd.DataFrame({"a": [1] * 3, "b": [1, 2, 3]}, index=[0, 1, 2])
tm.assert_frame_equal(result, expected)

result = df.nsmallest(3, "a")
expected = pd.DataFrame({"a": [1] * 3, "b": [1, 2, 3]})
tm.assert_frame_equal(result, expected)
