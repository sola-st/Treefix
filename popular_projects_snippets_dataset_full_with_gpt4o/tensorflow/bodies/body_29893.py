# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
a = array_ops.placeholder(dtypes_lib.float32, shape=None, name="a")
self.assertEqual("<tf.Tensor 'a:0' shape=<unknown> dtype=float32>", repr(a))

b = array_ops.placeholder(dtypes_lib.int32, shape=(32, 40), name="b")
self.assertEqual("<tf.Tensor 'b:0' shape=(32, 40) dtype=int32>", repr(b))

c = array_ops.placeholder(dtypes_lib.qint32, shape=(32, None, 2), name="c")
if c.shape._v2_behavior:
    self.assertEqual(
        "<tf.Tensor 'c:0' shape=(32, None, 2) dtype=qint32>", repr(c))
else:
    self.assertEqual(
        "<tf.Tensor 'c:0' shape=(32, ?, 2) dtype=qint32>", repr(c))
