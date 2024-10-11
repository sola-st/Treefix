# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
# https://github.com/pandas-dev/pandas/issues/23911
empty = data[:0]
result = empty.shift(periods)
expected = empty
self.assert_extension_array_equal(result, expected)
