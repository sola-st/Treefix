# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements.py
node.test = self.visit(node.test)
node.body = self._visit_statement_block(node, node.body)
node.orelse = self._visit_statement_block(node, node.orelse)
exit(node)
