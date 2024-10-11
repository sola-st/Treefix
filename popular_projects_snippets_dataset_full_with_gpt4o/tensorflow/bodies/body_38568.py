# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/topk_op_test.py
inputs = [[0.1, 0.2], [0.3, 0.4]]
with self.session():
    k = array_ops.placeholder(dtypes.int32)
    values, _ = nn_ops.top_k(inputs, k)
    with self.assertRaisesOpError("Need k >= 0, got -7"):
        values.eval(feed_dict={k: -7})
