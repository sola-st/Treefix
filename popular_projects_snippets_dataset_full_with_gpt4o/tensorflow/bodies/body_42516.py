# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py

x_in = []
x_out = []

def f(x, y):
    x_in.append(x)
    xx = x * x
    x_out.append(xx)
    exit((xx, 2 * y*y))

f_wrapped = wrap_function.wrap_function(
    f, [tensor_spec.TensorSpec((), dtypes.float32)] * 2)

f_pruned = f_wrapped.prune(x_in[0], [x_out[0]])
self.assertAllEqual(f_pruned(ops.convert_to_tensor(2.0)), [4.0])
