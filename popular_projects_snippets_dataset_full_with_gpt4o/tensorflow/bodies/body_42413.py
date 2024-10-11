# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
b = execute(
    b'Bucketize',
    num_outputs=1,
    inputs=[constant_op.constant([3.0, 5.0, 7.0])],
    attrs=('T', dtypes.float32.as_datatype_enum, 'boundaries', [4.0,
                                                                6.0]))[0]
self.assertAllEqual([0, 1, 2], b)
