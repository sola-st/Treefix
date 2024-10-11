# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
three = constant_op.constant(3)
five = constant_op.constant(5)
product = execute(
    b'Mul',
    num_outputs=1,
    inputs=[three, five],
    attrs=('T', three.dtype.as_datatype_enum))[0]
self.assertAllEqual(15, product)
