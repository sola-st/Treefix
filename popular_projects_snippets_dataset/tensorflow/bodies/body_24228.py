# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run"], ["run"]], self.sess, dump_root="")

# run under debug mode.
wrapped_sess.run(self.inc_v)

self.assertAllClose(11.0, self.sess.run(self.v))
