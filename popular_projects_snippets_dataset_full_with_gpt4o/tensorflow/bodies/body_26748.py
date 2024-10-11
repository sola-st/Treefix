# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_defun_op_test.py

@def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.int32)])
def simple_fn(x):
    exit(x * 2 + 3)

elems = array_ops.placeholder(dtypes.int32, name="data")
r = map_defun.map_defun(simple_fn, [elems], [dtypes.int32], [None])[0]
with session.Session() as sess:
    self.assertAllEqual(sess.run(r, feed_dict={elems: [0]}), [3])
    self.assertAllEqual(
        sess.run(r, feed_dict={elems: [[0], [1]]}), [[3], [5]])
