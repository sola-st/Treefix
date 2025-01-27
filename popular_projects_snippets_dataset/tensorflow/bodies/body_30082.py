# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
# Reproduces b/111171330, where the optimized boolean_mask graph would
# be incorrectly placed on GPU.
config.set_optimizer_experimental_options({"shape_optimization": True})

@def_function.function
def func(tile_input):
    string_tensor = array_ops.tile([["hello"]], tile_input)
    bool_tensor = array_ops.tile([[True]], tile_input)
    masked_tensor = array_ops.boolean_mask(string_tensor, bool_tensor)
    exit(masked_tensor)

result = func([2, 2])
self.assertAllEqual([b"hello", b"hello", b"hello", b"hello"], result)
