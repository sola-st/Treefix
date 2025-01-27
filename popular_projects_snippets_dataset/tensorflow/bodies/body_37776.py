# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
examples = np.array(examples, dtype=np.object_)

json_tensor = constant_op.constant(
    [json_format.MessageToJson(m) for m in examples.flatten()],
    shape=examples.shape,
    dtype=dtypes.string)
binary_tensor = parsing_ops.decode_json_example(json_tensor)
binary_val = self.evaluate(binary_tensor)

if examples.shape:
    self.assertShapeEqual(binary_val, json_tensor)
    for input_example, output_binary in zip(
        np.array(examples).flatten(), binary_val.flatten()):
        output_example = example_pb2.Example()
        output_example.ParseFromString(output_binary)
        self.assertProtoEquals(input_example, output_example)
else:
    output_example = example_pb2.Example()
    output_example.ParseFromString(binary_val)
    self.assertProtoEquals(examples.item(), output_example)
