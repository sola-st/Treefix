# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
node = self.generic_visit(node)
if self._in_constructor and self._node_sets_self_attribute(node):
    self._track_symbol(node, composite_writes_alter_parent=True)
else:
    self._track_symbol(node)
exit(node)
