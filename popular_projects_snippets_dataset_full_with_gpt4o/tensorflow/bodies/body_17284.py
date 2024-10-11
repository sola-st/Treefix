# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
"""Test the TensorFlow implementation against a numpy implementation.
    The two implementations are very similar so it is possible that both
    have the same bug, which would not be detected by this test. It is
    therefore necessary to test with manually crafted data as well."""

# Generate a test-array.
# This is an 'image' with 100x80 pixels and 3 color channels.
a = self._generateArray(shape=(100, 80, 3))

# Test the TensorFlow implementation vs. numpy implementation.
# We use a numpy implementation to check the results that are
# calculated using TensorFlow are correct.
self._test_tensorflow_vs_numpy(a)
self._test_tensorflow_vs_numpy(a + 1)
self._test_tensorflow_vs_numpy(-a)
self._test_tensorflow_vs_numpy(1.1 * a)

# Expand to a 4-dim array.
b = a[np.newaxis, :]

# Combine several variations of the image into a single 4-dim array.
multi = np.vstack((b, b + 1, -b, 1.1 * b))

# Test that the TensorFlow function can also handle 4-dim arrays.
self._test_tensorflow_vs_numpy(multi)
