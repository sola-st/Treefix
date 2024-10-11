# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/continue_statements.py
node.test = self.visit(node.test)
node.body = self._visit_loop_body(node, node.body)
# A continue in the else clause applies to the containing scope.
node.orelse = self._visit_non_loop_body(node.orelse)
exit(node)
