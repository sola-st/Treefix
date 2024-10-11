# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
assert not self._pending_statements
# It's important to visit node.items first, because any statements created
# thereby need to live outside the body.
for item in node.items:
    self.visit(item)
node.items = [self._ensure_node_in_anf(node, 'items', n)
              for n in node.items]
contexts_stmts = self._consume_pending_statements()
# This generic_visit will revisit node.items, but that is correct because by
# this point the node.items link has been checked.  It may be somewhat
# expensive if the configuration didn't call for transforming node.items, as
# then it may be large and will be uselessly transformed again.  This
# happens in several places.
node = self.generic_visit(node)
assert not self._pending_statements
contexts_stmts.append(node)
exit(contexts_stmts)
