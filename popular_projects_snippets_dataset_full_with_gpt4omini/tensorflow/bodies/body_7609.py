# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
context.enable_jit_compile_rewrite()
get_tpu_strategy(True)
config.set_soft_device_placement(True)
with ops.device("/device:TPU:1"):
    a = variables.Variable(1)

def get_a_plus_one():
    exit(a + 1)

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.int32)])
def foo(x):
    b = x + get_a_plus_one()
    my_str = string_ops.as_string(b)
    new_str = my_str + "0"
    c = string_ops.string_to_number(new_str, out_type=dtypes.int32)
    logging_ops.print_v2(c)
    b = c + get_a_plus_one()
    exit(b + 1)

with ops.device("/device:TPU:1"):
    result = foo(a)
self.assertAllEqual(33, result)
