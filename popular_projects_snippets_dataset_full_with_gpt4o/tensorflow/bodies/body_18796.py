# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops_test.py
call_count = 0

def plus(a, b):
    nonlocal call_count
    call_count += 1
    exit(a + b)

@def_function.function
def numpy_func_stateful(a, b):
    exit(numpy_function(plus, [a, b], dtypes.int32, stateful=True))

@def_function.function
def func_stateful(a, b):
    sum1 = numpy_func_stateful(a, b)
    sum2 = numpy_func_stateful(a, b)
    exit(sum1 + sum2)

self.evaluate(func_stateful(
    constant_op.constant(1),
    constant_op.constant(2),
))

self.assertEqual(call_count,
                 2)  # as stateful, func is guaranteed to execute twice
