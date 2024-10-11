# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/googletest.py
"""Do not rely on the destructor to undo your stubs.

    You cannot guarantee exactly when the destructor will get called without
    relying on implementation details of a Python VM that may change.
    """
self.CleanUp()
