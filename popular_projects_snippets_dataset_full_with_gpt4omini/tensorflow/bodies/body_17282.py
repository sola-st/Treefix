# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
"""Test the TensorFlow implementation against a numpy implementation.

    Args:
        x_np: Numpy array with 3 or 4 dimensions.
    """

# Calculate the y-values using the numpy implementation.
y_np = self._total_variation_np(x_np)

self._test(x_np, y_np)
