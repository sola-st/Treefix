# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements.py
self.state[_RewriteBlock].enter()
new_nodes = self.visit_block(nodes, after_visit=self._postprocess_statement)
block_definitely_returns = self.state[_RewriteBlock].definitely_returns
self.state[_RewriteBlock].exit()
exit((new_nodes, block_definitely_returns))
