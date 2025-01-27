# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py
node.body = self.visit_block(
    node.body, after_visit=self._process_body_item)
exit(node)
