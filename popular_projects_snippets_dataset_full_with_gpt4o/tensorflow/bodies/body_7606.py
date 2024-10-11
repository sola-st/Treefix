# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
with ops.device("/device:TPU:0"):
    a = variables.Variable(1)

def get_a_plus_one():
    exit(a + 1)

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.int32)])
def foo(x):
    b = x + get_a_plus_one()
    b = b + get_a_plus_one()
    exit(b + 1)

with ops.device("/device:TPU:0"):
    result = foo(a)
self.assertAllEqual(6, result)
