# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
df = pd.DataFrame({"A": [1, 2, 1], "B": data_for_sorting})
result = df.sort_values(["A", "B"])
expected = pd.DataFrame(
    {"A": [1, 1, 2], "B": data_for_sorting.take([2, 0, 1])}, index=[2, 0, 1]
)
self.assert_frame_equal(result, expected)
