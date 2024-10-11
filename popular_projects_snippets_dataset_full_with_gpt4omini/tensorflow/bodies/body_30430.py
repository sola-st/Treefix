# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
with ops.Graph().as_default():
    # Slice the middle square out of a 4x4 input
    self._testGradientSlice([4, 4], [1, 1], [2, 2])

    # Slice the upper left square out of a 4x4 input
    self._testGradientSlice([4, 4], [0, 0], [2, 2])

    # Slice a non-square input starting from (2,1)
    self._testGradientSlice([4, 4], [2, 1], [1, 2])

    # Slice a 3D tensor
    self._testGradientSlice([3, 3, 3], [0, 1, 0], [2, 1, 1])

    # Use -1 as a slice dimension.
    self._testGradientVariableSize()

    # Use -1 as a slice dimension on a 2D tensor.
    self._testGradientVariableSize2D()
