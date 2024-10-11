# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
for a, b in [(0, 0), (1, 0), (1, -1), (2, 3.5), (3.5, -2.25),
             (float("inf"), -2.25), (float("-inf"), -2.25),
             (3.5, float("nan"))]:
    test_binary_operation(a, b, op=lambda a, b: a + b, float_type=float_type)
