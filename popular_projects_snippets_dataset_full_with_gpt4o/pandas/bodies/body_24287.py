# Extracted from ./data/repos/pandas/pandas/io/common.py
"""
        Close all created buffers.

        Note: If a TextIOWrapper was inserted, it is flushed and detached to
        avoid closing the potentially user-created buffer.
        """
if self.is_wrapped:
    assert isinstance(self.handle, TextIOWrapper)
    self.handle.flush()
    self.handle.detach()
    self.created_handles.remove(self.handle)
for handle in self.created_handles:
    handle.close()
self.created_handles = []
self.is_wrapped = False
