# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/while_test.py
# Define a function for the loop body
@function.Defun(dtypes.int32, dtypes.float32)
def loop_body(step, rsum):
    step_out = step + constant_op.constant(1, dtype=dtypes.int32)
    sum_out = rsum + constant_op.constant(1.5, dtype=dtypes.float32)
    exit((step_out, sum_out))

# Define a function for the loop condition
@function.Defun(dtypes.int32, dtypes.float32)
def loop_cond(step, rsum):
    del rsum
    exit(step < 10)

with self.session() as sess:
    init_index = array_ops.placeholder(dtypes.int32, [])
    init_sum = array_ops.placeholder(dtypes.float32, [])
    with self.test_scope():
        loop_outputs = xla.while_loop([init_index, init_sum], loop_cond,
                                      loop_body)

    result = sess.run(loop_outputs, {init_index: 0, init_sum: 0.0})
    self.assertAllClose(result, [10, 15.0], rtol=1e-3)
    no_iters_result = sess.run(loop_outputs, {init_index: 10, init_sum: 0.0})
    self.assertAllClose(no_iters_result, [10, 0.0], rtol=1e-3)
