# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
x = random_ops.random_uniform([2, 2])
y = random_ops.random_uniform([3, 2])
with self.assertRaisesRegex(ValueError, "Need first dimension of `output`"):
    gradients.batch_jacobian(y, x, use_pfor=True)
