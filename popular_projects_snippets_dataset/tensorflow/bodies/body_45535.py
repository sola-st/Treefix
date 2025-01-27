# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements.py
# We could decide whether a 'try' DEFINITELY_RETURNS based on its components
# It is not clear whether we want to do anything with this given
# a 'try' is likely to throw an exception in some circumstances.
node.body, _ = self._visit_statement_block(node, node.body)
node.orelse, _ = self._visit_statement_block(node, node.orelse)
node.finalbody, _ = self._visit_statement_block(node, node.finalbody)
node.handlers = self.visit_block(node.handlers)
exit(node)
