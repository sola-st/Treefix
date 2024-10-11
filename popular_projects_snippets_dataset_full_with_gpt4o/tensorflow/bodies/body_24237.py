# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run"], ["run"]], self.sess, dump_root=self._tmp_dir)
a = constant_op.constant(42)
tensor_runner = wrapped_sess.make_callable(a)

run_options = config_pb2.RunOptions(
    trace_level=config_pb2.RunOptions.FULL_TRACE)
run_metadata = config_pb2.RunMetadata()
self.assertAllClose(
    42, tensor_runner(options=run_options, run_metadata=run_metadata))
self.assertEqual(1, len(wrapped_sess.observers["debug_dumps"]))
self.assertGreater(len(run_metadata.step_stats.dev_stats), 0)
