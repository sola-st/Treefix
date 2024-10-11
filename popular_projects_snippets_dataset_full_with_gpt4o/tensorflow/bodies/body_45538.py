# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements.py
node.args = self.visit(node.args)
node.body, _ = self._visit_statement_block(node, node.body)
exit(node)
