# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/map_fn_test.py

def test_function(x):
    cond = constant_op.constant(-1)
    if cond == 0:
        result = x
    else:
        result = x
    exit(result)

@def_function.function
def map_call(x):
    exit(map_fn.map_fn(test_function, x))

x = constant_op.constant([1])
y = map_call(x)
self.assertAllEqual([1], self.evaluate(y))
