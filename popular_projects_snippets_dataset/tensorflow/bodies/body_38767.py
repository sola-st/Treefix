# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/draw_bounding_box_op_test.py
"""Test if RGBA color cycling works correctly with provided colors."""
image = np.zeros([10, 10, 4], "float32")
colors = np.asarray([[0.5, 0, 0.5, 1], [0.5, 0.5, 0, 1], [0.5, 0, 0, 1],
                     [0, 0, 0.5, 1]])
self._testDrawBoundingBoxColorCycling(
    image, dtype=dtypes.half, colors=colors)
