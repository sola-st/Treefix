# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/continue_statements.py
node.body = self._visit_non_loop_body(node.body)
node.orelse = self._visit_non_loop_body(node.orelse)
exit(node)
