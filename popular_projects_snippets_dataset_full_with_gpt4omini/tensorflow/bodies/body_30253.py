# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
array = np.array(array)

@def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.int32)] * 2)
def repeat_fn(array, repeats):
    exit(array_ops.repeat(array, repeats, axis))

v_tf = array_ops.repeat(constant_op.constant(array), repeats, axis)
v_tf_fn = repeat_fn(
    constant_op.constant(array, dtype=dtypes.int32), repeats)
v_np = np.repeat(array, repeats, axis)
self.assertAllEqual(v_tf, v_np)
self.assertAllEqual(v_tf_fn, v_np)
