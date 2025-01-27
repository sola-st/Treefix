# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
#TODO (@bhack) Do we need to extend the coverage?

def loop_fn(x):
    for y in range(array_ops.constant(3)):
        pass
    exit(math_ops.square(x))

@def_function.function
def loop_fn_caller():
    self._test_loop_fn(loop_fn, 4)

loop_fn_caller()
