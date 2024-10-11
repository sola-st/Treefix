# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sort_ops_test.py
dtype = np.int64
self._testRandom_lowDimensionality(
    negative_axis=False, dtype=dtype, direction='ASCENDING')
self._testRandom_lowDimensionality(
    negative_axis=False, dtype=dtype, direction='DESCENDING')

# TODO(b/190410105) re-enable test once proper sort kernel is added.
if not test_util.is_asan_enabled() and not test_util.is_ubsan_enabled():
    edges = np.linspace(
        np.iinfo(dtype).min, np.iinfo(dtype).max, 10, dtype=dtype)
    self._test_sort(edges, 0, 'ASCENDING')
    self._test_sort(edges, 0, 'DESCENDING')
