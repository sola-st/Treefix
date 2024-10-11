# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/window_ops_test.py
try:
    exit(window_fn(window_length, periodic=periodic, dtype=dtype))
except TypeError:
    exit(window_fn(window_length, dtype=dtype))
