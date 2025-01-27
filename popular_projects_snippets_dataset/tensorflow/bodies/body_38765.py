# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/draw_bounding_box_op_test.py
"""Test if RGB color cycling works correctly with provided colors."""
image = np.zeros([10, 10, 3], "float32")
colors = np.asarray([[1, 1, 0, 1], [0, 0, 1, 1], [0.5, 0, 0.5, 1],
                     [0.5, 0.5, 0, 1], [0, 1, 1, 1], [1, 0, 1, 1]])
self._testDrawBoundingBoxColorCycling(image, colors=colors)
