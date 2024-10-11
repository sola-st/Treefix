# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
# num_outputs provided is 0, but one output is produced.
with self.assertRaises(errors.InvalidArgumentError):
    _ = execute(
        b'Mul',
        num_outputs=0,
        inputs=[constant_op.constant(3),
                constant_op.constant(5)],
        attrs=('T', dtypes.int32.as_datatype_enum))[0]
