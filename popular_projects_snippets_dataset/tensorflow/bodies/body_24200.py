# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
"""Attempt to wrap a non-Session-type object should cause an exception."""

wrapper = TestDebugWrapperSessionBadAction(self._sess)
with self.assertRaisesRegex(TypeError, "Expected type .*; got type .*"):
    TestDebugWrapperSessionBadAction(wrapper)
