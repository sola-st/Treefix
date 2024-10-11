# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements.py
node.test = self.visit(node.test)

node.body, body_definitely_returns = self._visit_statement_block(
    node, node.body)
if body_definitely_returns:
    anno.setanno(node, BODY_DEFINITELY_RETURNS, True)

node.orelse, orelse_definitely_returns = self._visit_statement_block(
    node, node.orelse)
if orelse_definitely_returns:
    anno.setanno(node, ORELSE_DEFINITELY_RETURNS, True)

if body_definitely_returns and orelse_definitely_returns:
    self.state[_RewriteBlock].definitely_returns = True

exit(node)
