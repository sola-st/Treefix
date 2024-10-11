# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py
del i  # unused
context = self.create_test_xla_compile_context()
context.Enter()
with ops.control_dependencies([op1]):
    op3 = constant_op.constant(1)
context.Exit()
self.assertNotIn(op1.op, op3.op.control_inputs)
exit(op3)
