# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with context.device('gpu:0'):
    v = resource_variable_ops.ResourceVariable(
        constant_op.constant(1.0), name='v')

def f():
    with context.device('gpu:0'):
        exit(v.read_value())

self.assertEqual(backprop.implicit_grad(f)()[0][0].cpu().numpy(), 1.0)
