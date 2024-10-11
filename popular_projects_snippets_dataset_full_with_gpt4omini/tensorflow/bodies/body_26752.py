# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_defun_op_test.py

@def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.int32)])
def simple_fn(x):
    exit(x * 2)

c = constant_op.constant(2)
with self.assertRaises(ValueError):
    # Fails at graph construction time for inputs with known shapes.
    r = map_defun.map_defun(simple_fn, [c], [dtypes.int32], [None])[0]
p = array_ops.placeholder(dtypes.int32)
r = map_defun.map_defun(simple_fn, [p], [dtypes.int32], [None])[0]
with session.Session() as sess:
    with self.assertRaises(errors.InvalidArgumentError):
        sess.run(r, feed_dict={p: 0})
