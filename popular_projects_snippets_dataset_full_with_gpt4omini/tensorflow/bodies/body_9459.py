# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/googletest.py
"""Reverses Set() calls, restoring things to their original definitions.

    This method is automatically called when the StubOutForTesting()
    object is deleted; there is no need to call it explicitly.

    It is okay to call UnsetAll() repeatedly, as later calls have no
    effect if no Set() calls have been made.
    """
# Undo calls to Set() in reverse order, in case Set() was called on the
# same arguments repeatedly (want the original call to be last one undone)
for (parent, old_child, child_name) in reversed(self.cache):
    setattr(parent, child_name, old_child)
self.cache = []
