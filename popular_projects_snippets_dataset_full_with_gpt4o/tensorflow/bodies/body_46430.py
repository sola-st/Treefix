# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
# Because the scopes are not isolated, processing any child block
# modifies the parent state causing the other child blocks to be
# processed incorrectly. So we need to checkpoint the parent scope so that
# each child sees the same context.
before_parent = Scope.copy_of(self.scope)
after_children = []
for child, scope_name in children:
    self.scope.copy_from(before_parent)
    parent = self._process_block_node(parent, child, scope_name)
    after_child = Scope.copy_of(self.scope)
    after_children.append(after_child)
for after_child in after_children:
    self.scope.merge_from(after_child)
exit(parent)
