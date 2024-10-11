# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements.py
node.items = self.visit_block(node.items)
node.body = self._visit_statement_block(node, node.body)
exit(node)
