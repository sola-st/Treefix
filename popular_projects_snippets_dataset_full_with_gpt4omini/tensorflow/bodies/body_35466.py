# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/multinomial_op_test.py
with test_util.use_gpu():
    x = random_ops.multinomial(array_ops.zeros([5, 0]), 7)
    with self.assertRaisesOpError("num_classes should be positive"):
        self.evaluate(x)
