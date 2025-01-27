# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
almost_equal = execute(
    b'ApproximateEqual',
    num_outputs=1,
    inputs=[constant_op.constant(3.0), constant_op.constant(2.9)],
    attrs=('tolerance', 0.3, 'T', dtypes.float32.as_datatype_enum))[0]
self.assertTrue(almost_equal)
