# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/draw_bounding_box_op_test.py
"""Test if drawing bounding box on a GRY image works."""
image = np.zeros([4, 4, 1], "float32")
self._testDrawBoundingBoxColorCycling(image)
