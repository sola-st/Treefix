# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
if invalid_indices:
    indices = constant_op.constant(
        [
            [0, 1, 0],
            [0, 1, 1],  # 0,1
            [1, 0, 0],  # 1,0
            [0, 0, 0],
            [0, 0, 2],  # 0,0
            [1, 1, 0],
            [1, 1, 1],
            [1, 1, 2],  # 1,1
            # 2,0
            [2, 1, 1]  # 2,1
            # 3,*
        ],
        dtypes.int64)
else:
    indices = constant_op.constant(
        [
            [0, 0, 0],
            [0, 0, 2],  # 0,0
            [0, 1, 0],
            [0, 1, 1],  # 0,1
            [1, 0, 0],  # 1,0
            [1, 1, 0],
            [1, 1, 1],
            [1, 1, 2],  # 1,1
            # 2,0
            [2, 1, 1]  # 2,1
            # 3,*
        ],
        dtypes.int64)
sp_a = sparse_tensor_lib.SparseTensor(
    indices,
    _constant(
        [
            1,
            9,  # 0,0
            3,
            3,  # 0,1
            1,  # 1,0
            9,
            7,
            8,  # 1,1
            # 2,0
            5  # 2,1
            # 3,*
        ],
        dtype),
    constant_op.constant([4, 2, 3], dtypes.int64))
sp_b = sparse_tensor_lib.SparseTensor(
    constant_op.constant(
        [
            [0, 0, 0],
            [0, 0, 3],  # 0,0
            # 0,1
            [1, 0, 0],  # 1,0
            [1, 1, 0],
            [1, 1, 1],  # 1,1
            [2, 0, 1],  # 2,0
            [2, 1, 1],  # 2,1
            [3, 0, 0],  # 3,0
            [3, 1, 0]  # 3,1
        ],
        dtypes.int64),
    _constant(
        [
            1,
            3,  # 0,0
            # 0,1
            3,  # 1,0
            7,
            8,  # 1,1
            2,  # 2,0
            5,  # 2,1
            4,  # 3,0
            4  # 3,1
        ],
        dtype),
    constant_op.constant([4, 2, 4], dtypes.int64))

if invalid_indices:
    with self.assertRaisesRegex(errors_impl.OpError, "out of order"):
        self._set_union(sp_a, sp_b)
else:
    expected_indices = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 0, 2],  # 0,0
        [0, 1, 0],  # 0,1
        [1, 0, 0],
        [1, 0, 1],  # 1,0
        [1, 1, 0],
        [1, 1, 1],
        [1, 1, 2],  # 1,1
        [2, 0, 0],  # 2,0
        [2, 1, 0],  # 2,1
        [3, 0, 0],  # 3,0
        [3, 1, 0],  # 3,1
    ]
    expected_values = _values(
        [
            1,
            3,
            9,  # 0,0
            3,  # 0,1
            1,
            3,  # 1,0
            7,
            8,
            9,  # 1,1
            2,  # 2,0
            5,  # 2,1
            4,  # 3,0
            4,  # 3,1
        ],
        dtype)
    expected_shape = [4, 2, 3]
    expected_counts = [
        [
            3,  # 0,0
            1  # 0,1
        ],
        [
            2,  # 1,0
            3  # 1,1
        ],
        [
            1,  # 2,0
            1  # 2,1
        ],
        [
            1,  # 3,0
            1  # 3,1
        ]
    ]

    intersection = self._set_union(sp_a, sp_b)
    self._assert_set_operation(
        expected_indices,
        expected_values,
        expected_shape,
        intersection,
        dtype=dtype)
    self.assertAllEqual(expected_counts, self._set_union_count(sp_a, sp_b))
