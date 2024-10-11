# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
"""White image should be returned for gamma equal

    to zero for uint8 images
    """
self._test_adjust_gamma_uint8(gamma=0.0)
