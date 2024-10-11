# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/continue_statements.py
node.items = self.visit_block(node.items)
node.body = self._visit_non_loop_body(node.body)
exit(node)
