# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with self.assertRaises(errors.InvalidArgumentError):
    execute(
        b'Identity',
        num_outputs=1,
        inputs=[constant_op.constant(3)],
        attrs=('T', dtypes.int32.as_datatype_enum, 'unknown_attr', 'blah'))
