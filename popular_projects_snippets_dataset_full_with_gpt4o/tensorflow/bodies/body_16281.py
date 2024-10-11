# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_bitcast_op_test.py
with self.assertRaisesRegex(exception, message):
    result = ragged_array_ops.bitcast(inputs, cast_to_dtype, name)
    self.evaluate(result)
