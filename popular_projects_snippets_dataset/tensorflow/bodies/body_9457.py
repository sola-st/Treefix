# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/googletest.py
"""Reverses SmartSet() calls, restoring things to original definitions.

    This method is automatically called when the StubOutForTesting()
    object is deleted; there is no need to call it explicitly.

    It is okay to call SmartUnsetAll() repeatedly, as later calls have
    no effect if no SmartSet() calls have been made.
    """
for args in reversed(self.stubs):
    setattr(*args)

self.stubs = []
