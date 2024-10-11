# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
json_tensor = constant_op.constant(["{]"])
if context.executing_eagerly():
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                "Error while parsing JSON"):
        parsing_ops.decode_json_example(json_tensor)
else:
    binary_tensor = parsing_ops.decode_json_example(json_tensor)
    with self.assertRaisesOpError("Error while parsing JSON"):
        self.evaluate(binary_tensor)
