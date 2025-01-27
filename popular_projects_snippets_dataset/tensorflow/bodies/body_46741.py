# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions.py
self._aggregate_predecessors_defined_in(node)
# TODO(mdan): Also track the exception type / name symbols.
node.body = self.visit_block(node.body)
exit(node)
