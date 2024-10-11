# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with self.assertRaises(errors.InvalidArgumentError):
    _ = execute(
        b'AddN',
        num_outputs=1,
        inputs=[constant_op.constant(3), constant_op.constant(4)],
        attrs=('T', dtypes.int32.as_datatype_enum, 'N', '2'))
