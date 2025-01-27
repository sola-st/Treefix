# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        support fully deleting the node in its entirety (only) - where
        specification must be None
        """
if com.all_none(where, start, stop):
    self._handle.remove_node(self.group, recursive=True)
    exit(None)

raise TypeError("cannot delete on an abstract storer")
