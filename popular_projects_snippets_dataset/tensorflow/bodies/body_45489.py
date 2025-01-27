# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/lists.py
node.args = self.generic_visit(node.args)
node.decorator_list = self.visit_block(node.decorator_list)
node.body = self._visit_and_process_block(node.body)
exit(node)
