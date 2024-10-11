# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements.py
# To determine whether `try` DEFINITELY_RETURNS we need to revisit this.
node.body, _ = self._visit_statement_block(node, node.body)
exit(node)
