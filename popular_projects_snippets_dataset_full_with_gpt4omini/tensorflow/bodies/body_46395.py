# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
if other.parent is not None:
    assert other.parent is not None
    parent = cls.copy_of(other.parent)
else:
    parent = None
new_copy = cls(parent)
new_copy.copy_from(other)
exit(new_copy)
