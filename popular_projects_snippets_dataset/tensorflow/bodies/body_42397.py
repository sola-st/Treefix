# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
# num_outputs provided is 50, but only one output is produced.
product = execute(
    b'Mul',
    num_outputs=50,
    inputs=[constant_op.constant(3),
            constant_op.constant(5)],
    attrs=('T', dtypes.int32.as_datatype_enum))[0]
self.assertAllEqual(15, product)
