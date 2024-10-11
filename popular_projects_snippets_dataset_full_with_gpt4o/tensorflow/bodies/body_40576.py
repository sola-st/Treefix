# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
old_context = context.context()
old_x = constant_op.constant(9.5)
context._set_context(context.Context())

try:
    new_x = constant_op.constant(9.5)
    self.assertEqual(new_x.numpy(), 9.5)
finally:
    context._set_context(old_context)

self.assertEqual(old_x.numpy(), 9.5)
