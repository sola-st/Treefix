# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
f = random_ops.random_normal([50, 5, 7, 10])
t = nn_ops.crelu(f)
self.assertEqual([50, 5, 7, 20], t.get_shape())
