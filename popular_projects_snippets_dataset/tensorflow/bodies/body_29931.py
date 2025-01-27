# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/stack_op_test.py
if not tf2.enabled():
    self.skipTest("only fails in TF2")

@def_function.function
def f():
    y = gen_array_ops.parallel_concat(values=[["tf"]], shape=0)
    exit(y)

with self.assertRaisesRegex(errors.InvalidArgumentError,
                            r"0th dimension of value .* is less than"):
    f()
