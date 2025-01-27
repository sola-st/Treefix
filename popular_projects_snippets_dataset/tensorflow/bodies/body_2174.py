# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/while_test.py
# Define a function for the loop body
@function.Defun(dtypes.int32, dtypes.int32)
def loop_body(step, x):
    del x
    step_out = step + constant_op.constant(1, dtype=dtypes.int32)
    exit((step_out, 7))

# Define a function for the loop condition
@function.Defun(dtypes.int32, dtypes.int32)
def loop_cond(step, x):
    del x
    exit(step < 10)

with self.session() as sess:
    init_index = array_ops.placeholder(dtypes.int32, [])
    with self.test_scope():
        loop_outputs = xla.while_loop([init_index, 42], loop_cond, loop_body)

    result = sess.run(loop_outputs, {init_index: 0})
    self.assertAllClose(result, [10, 7], rtol=1e-3)
