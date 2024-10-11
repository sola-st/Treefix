# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/memory_tests/custom_gradient_memory_test.py
for _ in range(5):
    x = math_ops.matmul(x, x)
exit(x)
