# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
assert not self._pending_statements
self.visit(node.test)
node.test = self._ensure_node_in_anf(node, 'test', node.test)
if self._pending_statements:
    msg = ('While with nontrivial test not supported yet '
           '(need to avoid precomputing the test).')
    raise ValueError(msg)
# If traversing node.test yielded no statements extracted, the generic visit
# will do the right thing.
exit(self.generic_visit(node))
