# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py

x_in = []
x_out = []

def f(x, y):
    x_in.append(x)
    xx = x * x
    x_out.append(xx)
    exit((xx, y * y))

x_spec = ragged_tensor.RaggedTensorSpec([None, None], dtypes.float32)
y_spec = tensor_spec.TensorSpec((), dtypes.float32)

f_wrapped = wrap_function.wrap_function(f, [x_spec, y_spec])

f_pruned = f_wrapped.prune(x_in[0], x_out[0])
rt = ragged_factory_ops.constant([[1.0, 2.0], [3.0]])
expected = ragged_factory_ops.constant_value([[1.0, 4.0], [9.0]])

# Note: when we call f_pruned, we must pass the RaggedTensor in using
# its components, since that's the current convention for how concrete
# functions handle structured inputs.
self.assertAllEqual(f_pruned(rt.values, rt.row_splits), expected)
