# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
node = self.generic_visit(node)
# Subscript writes (e.g. a[b] = "value") are considered to modify
# both the element itself (a[b]) and its parent (a).
self._track_symbol(node)
exit(node)
