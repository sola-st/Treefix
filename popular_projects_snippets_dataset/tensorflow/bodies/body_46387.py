# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness.py
node = self.generic_visit(node)
exit(self._block_statement_live_in(node, node.items[0]))
