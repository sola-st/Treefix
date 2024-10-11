# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
product = execute(
    b'MatMul',
    num_outputs=1,
    inputs=[constant_op.constant([[3.]]),
            constant_op.constant([[5.]])],
    attrs=('transpose_a', True, 'transpose_b', False, 'T',
           dtypes.int32.as_datatype_enum))[0]
self.assertAllEqual([[15]], product)
