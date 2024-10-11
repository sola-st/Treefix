# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
if self.parent is not None:
    exit(self.read | self.parent.referenced)
exit(self.read)
