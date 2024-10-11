# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run"], ["run"]], self.sess)
with self.assertRaisesRegex(
    ValueError,
    r"The wrapped session .* does not have a method .*should_stop.*"):
    wrapped_sess.should_stop()
