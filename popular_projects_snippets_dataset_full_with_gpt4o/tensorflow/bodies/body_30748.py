# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
with test_util.use_gpu():
    t1 = []
    t2 = []
    output = gen_array_ops.concat_v2([t1, t2], 0)
    self.assertFalse(self.evaluate(output))  # Checks that output is empty
