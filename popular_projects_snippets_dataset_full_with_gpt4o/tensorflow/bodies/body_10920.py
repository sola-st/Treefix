# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
exit(ops.convert_to_tensor(
    sum(math_ops.matmul(rng.rand(k, k), x) for x in xs)
    + rng.rand(k, k)))
