# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run"]], self.sess, dump_root="")

run_output = wrapped_sess.run({"foo": {"baz": []}, "bar": ()})
self.assertEqual({"foo": {"baz": []}, "bar": ()}, run_output)
