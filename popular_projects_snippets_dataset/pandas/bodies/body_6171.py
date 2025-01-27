# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
# https://github.com/pandas-dev/pandas/issues/22386
subset = data[:5]
data = pd.Series(subset, name="A")
expected = pd.Series(subset.take(indices, allow_fill=True), name="A")

if frame:
    result = data.to_frame(name="A").assign(B=1).shift(periods)
    expected = pd.concat(
        [expected, pd.Series([1] * 5, name="B").shift(periods)], axis=1
    )
    compare = self.assert_frame_equal
else:
    result = data.shift(periods)
    compare = self.assert_series_equal

compare(result, expected)
