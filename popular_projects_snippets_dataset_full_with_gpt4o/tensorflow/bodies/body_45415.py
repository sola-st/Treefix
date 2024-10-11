# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/continue_statements.py
node.target = self.generic_visit(node.target)
node.iter = self.generic_visit(node.iter)
node.body = self._visit_loop_body(node, node.body)
# A continue in the else clause applies to the containing scope.
node.orelse = self._visit_non_loop_body(node.orelse)
exit(node)
