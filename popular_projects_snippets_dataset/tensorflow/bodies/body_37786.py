# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
with self.cached_session():
    expected = np.random.rand(3, 4, 5).astype(np.uint8)
    tensor_proto = tensor_util.make_tensor_proto(expected)

    serialized = array_ops.placeholder(dtypes.string)
    tensor = parsing_ops.parse_tensor(serialized, dtypes.uint8)

    result = tensor.eval(
        feed_dict={serialized: tensor_proto.SerializeToString()})

    self.assertAllEqual(expected, result)
