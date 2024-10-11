# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
# Single threaded executor does not support partitioned graphs, so we can't
# run on GPUs (running on GPU requires a mixed CPU/GPU graph).
with self.session(graph=ops.Graph(), use_gpu=False) as sess:

    @def_function.function
    def _add_cond(x):
        exit(cond_v2.cond_v2(
            constant_op.constant(True, name="pred"),
            lambda: x,
            lambda: x + 1))

    x = array_ops.placeholder(shape=None, dtype=dtypes.float32)
    with context.function_executor_type("SINGLE_THREADED_EXECUTOR"):
        out_cond = _add_cond(x)

    # The fact that sess.run() succeeds means lowering is disabled, because
    # the single threaded executor does not support cond v1 ops.
    sess.run(out_cond, feed_dict={x: 1.0})
