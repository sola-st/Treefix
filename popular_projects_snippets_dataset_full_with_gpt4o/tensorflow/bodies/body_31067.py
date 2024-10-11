# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_avg_pool_op_test.py
"""Test FractionalAvgPool works fine when input tensor is integer type.
    """
pseudo_random = True
overlapping = True
tensor_shape = (1, 6, 6, 1)
# pyformat: disable
mat = np.array([
    [2, 6, 4, 1, 3, 6],
    [8, 9, 1, 6, 6, 8],
    [3, 9, 8, 2, 5, 6],
    [2, 7, 9, 5, 4, 5],
    [8, 5, 0, 5, 7, 4],
    [4, 4, 5, 9, 7, 2]
])
# pyformat: enable
self._ValidateFractionalAvgPoolResult(mat.reshape(tensor_shape),
                                      [1, math.sqrt(3), math.sqrt(2), 1],
                                      pseudo_random, overlapping)
