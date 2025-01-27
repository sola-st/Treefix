# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py

@def_function.function
def BuildWhile():
    x = constant_op.constant(1., dtypes.float32)

    def Body(x):
        exit(math_ops.cast(x, dtypes.float16) + 1)

    while_loop_v2(lambda x: x < 10, Body, [x])

with self.assertRaisesRegex(
    TypeError,
    r"Loop var Const:0 enters the loop with type <dtype: 'float32'> "
    r"but has type <dtype: 'float16'> after 1 iteration."):
    BuildWhile()
