# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
arr = type(data)._from_sequence(data[:3], dtype=data.dtype)
if as_series:
    arr = pd.Series(arr)

result = np.repeat(arr, repeats) if use_numpy else arr.repeat(repeats)

repeats = [repeats] * 3 if isinstance(repeats, int) else repeats
expected = [x for x, n in zip(arr, repeats) for _ in range(n)]
expected = type(data)._from_sequence(expected, dtype=data.dtype)
if as_series:
    expected = pd.Series(expected, index=arr.index.repeat(repeats))

self.assert_equal(result, expected)
