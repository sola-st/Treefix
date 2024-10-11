# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
# https://github.com/pandas-dev/pandas/issues/23911
subset = data[:2]
result = subset.shift(periods)
expected = subset.take(indices, allow_fill=True)
self.assert_extension_array_equal(result, expected)
