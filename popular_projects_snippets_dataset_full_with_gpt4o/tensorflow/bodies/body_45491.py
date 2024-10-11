# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/lists.py
node.test = self.visit(node.test)
node.body = self._visit_and_process_block(node.body)
node.orelse = self._visit_and_process_block(node.orelse)
exit(node)
