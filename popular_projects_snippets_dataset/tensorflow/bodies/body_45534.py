# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements.py
node.items = self.visit_block(node.items)
node.body, definitely_returns = self._visit_statement_block(node, node.body)
if definitely_returns:
    anno.setanno(node, STMT_DEFINITELY_RETURNS, True)
exit(node)
