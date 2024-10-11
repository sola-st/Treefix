# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py

@def_function.function(autograph=False)
def f():
    exit(array_ops.boolean_mask([1, 2, 3], [True, False, True],
                                  axis=constant_op.constant(
                                      0, dtype=dtypes.int32)))

self.assertAllEqual(self.evaluate(f()), [1, 3])
