# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/lists.py
node.target = self.visit(node.target)
node.body = self._visit_and_process_block(node.body)
node.orelse = self._visit_and_process_block(node.orelse)
exit(node)
