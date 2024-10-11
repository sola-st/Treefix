# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
if invalid_indices:
    indices = constant_op.constant([
        [0, 1, 0], [0, 1, 1],             # 0,1
        [1, 0, 0],                        # 1,0
        [1, 1, 0], [1, 1, 1], [1, 1, 2],  # 1,1
        [0, 0, 0], [0, 0, 2],             # 0,0
                                          # 2,0
        [2, 1, 1]                         # 2,1
    ], dtypes.int64)
else:
    indices = constant_op.constant([
        [0, 0, 0], [0, 0, 2],             # 0,0
        [0, 1, 0], [0, 1, 1],             # 0,1
        [1, 0, 0],                        # 1,0
        [1, 1, 0], [1, 1, 1], [1, 1, 2],  # 1,1
                                          # 2,0
        [2, 1, 1]                         # 2,1
    ], dtypes.int64)

sp = sparse_tensor_lib.SparseTensor(
    indices,
    _constant([
        1, 9,     # 0,0
        3, 3,     # 0,1
        1,        # 1,0
        9, 7, 8,  # 1,1
                  # 2,0
        5         # 2,1
    ], dtype),
    constant_op.constant([3, 2, 3], dtypes.int64))

if invalid_indices:
    with self.assertRaisesRegex(errors_impl.OpError, "out of order"):
        self._set_size(sp)
else:
    self.assertAllEqual([
        [2,   # 0,0
         1],  # 0,1
        [1,   # 1,0
         3],  # 1,1
        [0,   # 2,0
         1]   # 2,1
    ], self._set_size(sp))
