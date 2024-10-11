# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
assert not self._pending_statements
# It's important to visit node.iter first, because any statements created
# thereby need to live outside the body.
self.visit(node.iter)
node.iter = self._ensure_node_in_anf(node, 'iter', node.iter)
iter_stmts = self._consume_pending_statements()
# This generic_visit will revisit node.iter, but that is correct because by
# this point the node.iter link has been checked.  It may be somewhat
# expensive if the configuration didn't call for transforming node.iter, as
# then it may be large and will be uselessly transformed again.  This
# behavior is what causes the documented effect that configuration callables
# may be invoked more than once of the same links; if the code is rewritten
# not to do that (anywhere), the docstring of `transform` should be updated.
node = self.generic_visit(node)
assert not self._pending_statements
iter_stmts.append(node)
exit(iter_stmts)
