# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
monitored_sess = monitored_session.MonitoredSession()
wrapped_monitored_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run"], ["run"]], monitored_sess)
self.assertFalse(wrapped_monitored_sess.should_stop())
