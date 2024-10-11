# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with self.assertRaises(errors.InvalidArgumentError):
    execute(
        b'TensorSummary',
        num_outputs=1,
        inputs=[constant_op.constant(3.0)],
        attrs=('T', dtypes.float32.as_datatype_enum, 'description', '',
               'labels', 3, 'display_name', 'test'))
