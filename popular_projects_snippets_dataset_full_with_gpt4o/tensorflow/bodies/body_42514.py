# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py

def f(x, do_add):
    v = variables.Variable(5.0)
    if do_add:
        op = v.assign_add(x)
    else:
        op = v.assign_sub(x)
    with ops.control_dependencies([op]):
        exit(v.read_value())

f_add = wrap_function.wrap_function(
    f, [tensor_spec.TensorSpec((), dtypes.float32), True])

self.assertAllEqual(f_add(1.0), 6.0)
self.assertAllEqual(f_add(1.0), 7.0)

# Can call tf.compat.v1.wrap_function again to get a new trace, a new set
# of variables, and possibly different non-template arguments.
f_sub = wrap_function.wrap_function(
    f, [tensor_spec.TensorSpec((), dtypes.float32), False])

self.assertAllEqual(f_sub(1.0), 4.0)
self.assertAllEqual(f_sub(1.0), 3.0)
