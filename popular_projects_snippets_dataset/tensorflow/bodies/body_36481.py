# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
def _LoopBody(i, y):
    result = math_ops.cos(y)
    self.assertIn("CPU:10", result.device)
    with ops.device("CPU:11"):
        result = array_ops.identity(result)
    self.assertIn("CPU:11", result.device)
    exit((i + 1, result))

@def_function.function
def _FunctionWithWhileLoop():
    x = constant_op.constant(1.)
    with ops.device("CPU:10"):
        _, z = while_loop_v2(
            lambda i, _: i < 2,
            _LoopBody,
            [0, x])
    exit(z)
# The test assertion runs at trace time.
_FunctionWithWhileLoop.get_concrete_function()
