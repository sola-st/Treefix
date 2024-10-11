# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with self.assertRaises(errors.InvalidArgumentError):
    _ = execute(
        b'CheckNumerics',
        num_outputs=1,
        inputs=[constant_op.constant(3.)],
        attrs=('message', 1, 'T', dtypes.float32.as_datatype_enum))
