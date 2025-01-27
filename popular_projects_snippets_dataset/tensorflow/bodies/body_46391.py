# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
assert self.is_final
if self.parent is not None and not self.isolated:
    exit(self.parent)
exit(self)
