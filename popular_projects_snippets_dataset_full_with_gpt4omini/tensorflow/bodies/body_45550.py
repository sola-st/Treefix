# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements.py
node.body = self._visit_statement_block(node, node.body)
node.orelse = self._visit_statement_block(node, node.orelse)
node.finalbody = self._visit_statement_block(node, node.finalbody)
node.handlers = self.visit_block(node.handlers)
exit(node)
