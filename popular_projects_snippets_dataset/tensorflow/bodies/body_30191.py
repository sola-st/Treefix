# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
res = array_ops.sequence_mask(constant_op.constant([0, 1, 4]))
self.assertAllEqual(res.get_shape().as_list(), [3, 4])
self.assertAllEqual(res,
                    [[False, False, False, False],
                     [True, False, False, False], [True, True, True, True]])
