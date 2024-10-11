# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
x = constant_op.constant(1.).gpu()
with context.device('gpu:0'):
    y = constant_op.constant(2.)
# Add would fail if t2 were not on GPU
result = execute(
    b'Add', 1, inputs=[x, y],
    attrs=('T', x.dtype.as_datatype_enum))[0].cpu().numpy()
self.assertEqual(3, result)
