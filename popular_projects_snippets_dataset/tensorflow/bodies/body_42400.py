# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
three = constant_op.constant([[3.]]).gpu()
five = constant_op.constant([[5.]]).gpu()
with ops.device('CPU:0'):
    product = execute(
        b'MatMul',
        num_outputs=1,
        inputs=[three, five],
        attrs=('transpose_a', False, 'transpose_b', False, 'T',
               three.dtype.as_datatype_enum))[0]
    self.assertAllEqual([[15.0]], product)
