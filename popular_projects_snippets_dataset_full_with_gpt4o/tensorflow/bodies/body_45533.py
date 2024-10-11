# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements.py
node.iter = self.visit(node.iter)
node.target = self.visit(node.target)
node.body, _ = self._visit_statement_block(node, node.body)
node.orelse, _ = self._visit_statement_block(node, node.orelse)
exit(node)
