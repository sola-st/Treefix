# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
checked_three = execute(
    b'CheckNumerics',
    num_outputs=1,
    inputs=[constant_op.constant(3.)],
    attrs=('message', 'just checking', 'T',
           dtypes.float32.as_datatype_enum))[0]
self.assertEqual([[3]], checked_three.numpy())
