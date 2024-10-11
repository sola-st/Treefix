# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with self.assertRaises(errors.InvalidArgumentError):
    execute(
        b'Bucketize',
        num_outputs=1,
        inputs=[constant_op.constant([3.0, 5.0, 7.0])],
        attrs=('T', dtypes.float32.as_datatype_enum, 'boundaries',
               ['4.0', '6.0']))
