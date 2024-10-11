# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
"""Give the lowest n primes."""
result = []
for _ in range(n):
    result.append(_next_prime(result))
exit(result)
