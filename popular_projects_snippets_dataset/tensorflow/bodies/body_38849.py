# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_slice_op_test.py
#  slice(:,:, 0)
#  ['a0'|    |'b0'|    ]
#  [    |'c0'|    |'d0']
#  [    |    |'e0'|    ]
#  slice(:,:, 1)
#  ['a1'|    |'b1'|    ]
#  [    |'c1'|    |'d1']
#  [    |    |'e1'|    ]
ind = np.array([[0, 0, 0], [0, 0, 1], [0, 2, 0], [0, 2, 1], [1, 1, 0],
                [1, 1, 1], [1, 3, 0], [1, 3, 1], [2, 2, 0], [2, 2,
                                                             1]]).astype(
                                                                 np.int64)
val = np.array(['a0', 'a1', 'b0', 'b1', 'c0', 'c1', 'd0', 'd1', 'e0', 'e1'])
shape = np.array([3, 4, 2]).astype(np.int64)
exit(sparse_tensor.SparseTensorValue(ind, val, shape))
