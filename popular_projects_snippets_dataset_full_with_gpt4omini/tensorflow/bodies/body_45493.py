# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/lists.py
node.items = self.visit_block(node.items)
node.body = self._visit_and_process_block(node.body)
exit(node)
