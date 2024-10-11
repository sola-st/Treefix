# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
x = constant_op.constant(1.0, name="x")
y = constant_op.constant(2.0, name="y")

def true_fn():
    exit(2.0)

def false_fn():

    @def_function.function
    def fn():

        @def_function.function
        def nested_fn():
            exit(x * y * 2.0)

        exit(nested_fn())

    exit(fn())

self._testCond(true_fn, false_fn, [x])
self._testCond(true_fn, false_fn, [x, y])
self._testCond(true_fn, false_fn, [y])
