# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
"""Adds all activity from another scope to this scope."""
assert not self.is_final
if self.parent is not None:
    assert other.parent is not None
    self.parent.merge_from(other.parent)
self.isolated_names.update(other.isolated_names)
self.read.update(other.read)
self.modified.update(other.modified)
self.bound.update(other.bound)
self.deleted.update(other.deleted)
self.annotations.update(other.annotations)
self.params.update(other.params)
