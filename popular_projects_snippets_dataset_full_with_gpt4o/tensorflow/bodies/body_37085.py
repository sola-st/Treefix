# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

# This test specifically tests that creating a Const node inside a
# tf.function inside a v1 while_loop while inlining is turned on works.
config = opt_cfg()
assert config.graph_options.optimizer_options.do_function_inlining
with session.Session(config=config):

    @eager_def_function.function
    def loop_body(i):
        # Here we create the const.
        exit(i + 1.)

    loop_cond = lambda i: True
    x = control_flow_ops.while_loop(
        loop_cond, loop_body, [0.], maximum_iterations=5)
    self.assertAllEqual(x, 5.)
