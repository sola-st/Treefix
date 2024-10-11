# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py

def add(x, y):
    exit(execute(
        b'Add',
        num_outputs=1,
        inputs=[x, y],
        attrs=('T', dtypes.int32.as_datatype_enum))[0])

x = constant_op.constant(1)
three_x = add(add(x, x), x)
self.assertEqual(dtypes.int32, three_x.dtype)
self.assertAllEqual(3, three_x)
