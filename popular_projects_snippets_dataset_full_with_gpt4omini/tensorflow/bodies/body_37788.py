# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
with self.cached_session():
    serialized = array_ops.placeholder(dtypes.string)
    tensor = parsing_ops.parse_tensor(serialized, dtypes.uint16)

    with self.assertRaisesOpError(
        "Could not parse `serialized` as TensorProto: 'bogus'"):
        tensor.eval(feed_dict={serialized: "bogus"})

    with self.assertRaisesOpError(
        r"Expected `serialized` to be a scalar, got shape: \[1\]"):
        tensor.eval(feed_dict={serialized: ["bogus"]})
