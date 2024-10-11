# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
"""Inlined functions must not execute in a untaken control flow branch."""

@function.Defun(dtypes.int32)
def AssertFail(x):
    # Assertion that always fails and does not have a data dependency on `x`.
    assert_false = control_flow_ops.Assert(False, [42])
    with ops.control_dependencies([assert_false]):
        exit(array_ops.identity(x))

with ops.device("CPU"):
    pred = array_ops.placeholder(dtypes.bool)
    x = array_ops.placeholder(dtypes.int32)
    cond = control_flow_ops.cond(pred, lambda: x + 1, lambda: AssertFail(x))
    # pylint: disable=unnecessary-lambda
    loop = control_flow_ops.while_loop(lambda y: pred,
                                       lambda y: AssertFail(y), [x])
    # pylint: enable=unnecessary-lambda

rewriter_config = rewriter_config_pb2.RewriterConfig(
    dependency_optimization=rewriter_config_pb2.RewriterConfig.OFF)
# Enables inlining.
config = config_pb2.ConfigProto(
    graph_options=config_pb2.GraphOptions(
        optimizer_options=config_pb2.OptimizerOptions(
            opt_level=config_pb2.OptimizerOptions.L0,
            do_common_subexpression_elimination=True,
            do_function_inlining=True,
            do_constant_folding=True),
        rewrite_options=rewriter_config))

with session.Session(config=config) as sess:
    # Since the 'False' branch is not taken, the assertion should not fire.
    self.assertEqual(4, sess.run(cond, {pred: True, x: 3}))

    # The assertion should still fire if the False branch is taken.
    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                "assertion"):
        sess.run(cond, {pred: False, x: 3})

    # Similarly for loops.
    self.assertEqual(3, sess.run(loop, {pred: False, x: 3}))
    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                "assertion"):
        sess.run(loop, {pred: True, x: 3})
