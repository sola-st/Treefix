# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with self.assertRaises(errors.InvalidArgumentError):
    _ = execute(
        b'ApproximateEqual',
        num_outputs=1,
        inputs=[constant_op.constant(3.0), constant_op.constant(2.9)],
        attrs=('tolerance', '0.3', 'T', dtypes.float32.as_datatype_enum))
