# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with self.assertRaises(errors.InvalidArgumentError):
    execute(
        b'Squeeze',
        num_outputs=1,
        inputs=[constant_op.constant([[[3.0]]])],
        attrs=('T', dtypes.float32.as_datatype_enum, 'squeeze_dims', 0))
