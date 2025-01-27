# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
# Special rules for AugAssign. Here, the AST only shows the target as
# written, when it is in fact also read.
self._enter_scope(False)

self._in_aug_assign = True
node.target = self.visit(node.target)
self._in_aug_assign = False

node.op = self.visit(node.op)
node.value = self.visit(node.value)
self._exit_and_record_scope(node)
exit(node)
