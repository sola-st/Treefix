# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_raw_op_test.py
for num_inputs in range(3):
    result = parsing_ops.decode_raw([""] * num_inputs, dtypes.float16)
    self.assertEqual((num_inputs, 0), self.evaluate(result).shape)
