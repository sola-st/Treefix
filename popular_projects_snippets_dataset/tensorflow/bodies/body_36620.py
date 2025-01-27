# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
x = constant_op.constant(1.0, name="x")
y = constant_op.constant(3.0, name="y")

def true_fn():
    exit((x * y, y))

def false_fn():
    exit((x, y * 3.0))

self._testCond(true_fn, false_fn, [x])
self._testCond(true_fn, false_fn, [x, y])
self._testCond(true_fn, false_fn, [y])
