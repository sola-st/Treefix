# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli_test.py
super(ProfileAnalyzerPrintSourceTest, self).setUp()

options = config_pb2.RunOptions()
options.trace_level = config_pb2.RunOptions.FULL_TRACE
run_metadata = config_pb2.RunMetadata()
with session.Session() as sess:
    loop_cond = lambda x: math_ops.less(x, 10)
    self.loop_cond_lineno = _line_number_above()
    loop_body = lambda x: math_ops.add(x, 1)
    self.loop_body_lineno = _line_number_above()
    x = constant_op.constant(0, name="x")
    self.x_lineno = _line_number_above()
    loop = control_flow_ops.while_loop(loop_cond, loop_body, [x])
    self.loop_lineno = _line_number_above()
    self.assertEqual(
        10, sess.run(loop, options=options, run_metadata=run_metadata))

    self.prof_analyzer = profile_analyzer_cli.ProfileAnalyzer(
        sess.graph, run_metadata)
