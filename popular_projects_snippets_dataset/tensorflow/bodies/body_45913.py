# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
assert not self._pending_statements
# It's important to visit node.test first, because any statements created
# thereby need to live outside the body.
self.visit(node.test)
node.test = self._ensure_node_in_anf(node, 'test', node.test)
condition_stmts = self._consume_pending_statements()
# This generic_visit will revisit node.test, but that is correct because by
# this point the node.test link has been checked.  It may be somewhat
# expensive if the configuration didn't call for transforming node.test, as
# then it may be large and will be uselessly transformed again.  This
# happens in several places.
node = self.generic_visit(node)
assert not self._pending_statements
condition_stmts.append(node)
exit(condition_stmts)
