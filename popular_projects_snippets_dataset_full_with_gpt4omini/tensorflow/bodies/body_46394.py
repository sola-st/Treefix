# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
"""Recursively copies the contents of this scope from another scope."""
assert not self.is_final
if self.parent is not None:
    assert other.parent is not None
    self.parent.copy_from(other.parent)
self.isolated_names = copy.copy(other.isolated_names)
self.modified = copy.copy(other.modified)
self.read = copy.copy(other.read)
self.deleted = copy.copy(other.deleted)
self.bound = copy.copy(other.bound)
self.annotations = copy.copy(other.annotations)
self.params = copy.copy(other.params)
