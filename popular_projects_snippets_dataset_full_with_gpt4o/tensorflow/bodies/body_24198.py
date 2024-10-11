# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
"""The wrapper should work also on other subclasses of session.Session."""

TestDebugWrapperSession(
    session.InteractiveSession(), self._dump_root, self._observer)
