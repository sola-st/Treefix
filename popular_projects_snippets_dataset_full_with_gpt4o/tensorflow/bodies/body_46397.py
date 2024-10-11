# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
"""Freezes this scope."""
assert not self.is_final
# TODO(mdan): freeze read, modified, bound.
if self.parent is not None:
    assert not self.parent.is_final
    if not self.isolated:
        self.parent.read.update(self.read - self.isolated_names)
        self.parent.modified.update(self.modified - self.isolated_names)
        self.parent.bound.update(self.bound - self.isolated_names)
        self.parent.globals.update(self.globals)
        self.parent.nonlocals.update(self.nonlocals)
        self.parent.annotations.update(self.annotations)
    else:
        # TODO(mdan): This is not accurate.
        self.parent.read.update(self.read - self.bound)
        self.parent.annotations.update(self.annotations - self.bound)
self.is_final = True
