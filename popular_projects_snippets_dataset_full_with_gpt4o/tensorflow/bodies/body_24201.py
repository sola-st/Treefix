# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
with self.assertRaisesRegex(
    ValueError, "Invalid OnSessionInitAction value: nonsense_action"):
    TestDebugWrapperSessionBadAction(
        self._sess, bad_init_action="nonsense_action")
