# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees.py
# Context manager calls (in node.items) are not converted.
node.body = self.visit_block(node.body)
exit(node)
