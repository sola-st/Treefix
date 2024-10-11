# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with context.execution_mode(context.ASYNC):
    three = constant_op.constant(3)
    five = constant_op.constant(5)
    product = execute(
        b'Mul',
        num_outputs=1,
        inputs=[three, five],
        attrs=('T', three.dtype.as_datatype_enum))[0]
    self.assertAllEqual(15, product)
# Error: Invalid arguments
# TODO(b/149995282): When an exception is thrown in ASYNC mode, it seems
# there are things left over that cause mutex corruption when
# _reset_context() is called before the next test is executed.
#
# context.set_execution_mode(context.ASYNC)
# with self.assertRaises(errors.InvalidArgumentError):
#   execute(
#       b'MatMul',
#       num_outputs=1,
#       inputs=[three, five],
#       attrs=('transpose_a', False, 'transpose_b', False, 'T',
#              three.dtype.as_datatype_enum))
#   context.context().executor.wait()
#
context.context().executor.clear_error()
context.context().execution_mode = context.SYNC
