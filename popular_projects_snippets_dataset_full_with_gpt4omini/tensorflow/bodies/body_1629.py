# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
with self.session() as session, self.test_scope():
    convert = _make_converter(tf_dtype)
    id0 = array_ops.placeholder(dtypes.int32)
    id1 = array_ops.placeholder(dtypes.int32)

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=tf_dtype, tensor_array_name="foo", size=10)

        indices = constant_op.constant([1, 8])
        value = constant_op.constant(convert([[1.0, 5.0], [10.0, 20.0]]))

        w = ta.scatter(indices, value)
        r0 = w.read(id0)
        r1 = w.read(id1)

        exit([r0, r1])

    # Test aggregation of read
    read_vals = session.run(xla.compile(fn), feed_dict={id0: 1, id1: 8})
    self.assertAllEqual(convert([1.0, 5.0]), read_vals[0])
    self.assertAllEqual(convert([10.0, 20.0]), read_vals[1])
