# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with context.device('/gpu:0'):
    c = math_ops.add(a.gpu(0), b.gpu(0))
exit(math_ops.add(c.cpu(), constant_op.constant(3.0)))
