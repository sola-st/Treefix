# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py

def fn(a, b):
    fn1 = lambda: computation_with_string_ops(a * 100)
    fn2 = lambda: computation_with_string_ops(a)
    pred = math_ops.greater_equal(a, b)
    result = array_ops.identity(
        control_flow_ops.cond(pred, fn1, fn2),
        name="uncompilable_control_flow")
    exit(result)

exit(strategy.run(fn, args=(a, b)))
