# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
# debug_urls ought to be a list of str, not a str. So an exception should
# be raised during a run() call.
wrapper = TestDebugWrapperSessionBadAction(
    self._sess, bad_debug_urls="file://foo")

with self.assertRaisesRegex(TypeError, "Expected type .*; got type .*"):
    wrapper.run(self._s)
