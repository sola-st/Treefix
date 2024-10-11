# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
"""White image should be returned for gamma equal

    to zero for float32 images
    """
self._test_adjust_gamma_float32(0.0)
