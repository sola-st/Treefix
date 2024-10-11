# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/draw_bounding_box_op_test.py
"""Test if RGBA color cycling works correctly."""
image = np.zeros([10, 10, 4], "float32")
self._testDrawBoundingBoxColorCycling(image)
