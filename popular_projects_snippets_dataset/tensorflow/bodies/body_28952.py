# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
for i in range(1, 10):
    exit(([i] * i, [i, i ** 2, i ** 3]))
