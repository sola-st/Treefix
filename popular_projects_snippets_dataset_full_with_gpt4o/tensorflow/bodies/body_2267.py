# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
# Verify that accumulation happens in the specified output type int32 by
# using a result (16 * 16 * 16) that doesn't fit in int8.
self._testBinary(
    lambda x, y: math_ops.matmul(x, y, output_type=np.int32),
    np.tile(np.array([[[16]]], dtype=np.int8), (1, 1, 16)),
    np.tile(np.array([[[16]]], dtype=np.int8), (1, 16, 1)),
    expected=np.array([[[16 * 16 * 16]]], dtype=np.int32))
