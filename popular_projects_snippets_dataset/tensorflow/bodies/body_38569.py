# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/topk_op_test.py
inputs = [[0.1, 0.2], [0.3, 0.4]]
with self.assertRaisesRegex(ValueError,
                            r"must have last dimension >= k = 4"):
    nn_ops.top_k(inputs, 4)
