# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/continue_statements.py
node.body = self._visit_non_loop_body(node.body)
node.orelse = self._visit_non_loop_body(node.orelse)
# In Python 3.8 and later continue is allowed in finally blocks
node.finalbody = self._visit_non_loop_body(node.finalbody)
node.handlers = self.visit_block(node.handlers)
exit(node)
