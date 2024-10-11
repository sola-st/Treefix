# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
wrapper = TestDebugWrapperSessionBadAction(
    self._sess, bad_run_start_action="nonsense_action")

with self.assertRaisesRegex(
    ValueError, "Invalid OnRunStartAction value: nonsense_action"):
    wrapper.run(self._s)
