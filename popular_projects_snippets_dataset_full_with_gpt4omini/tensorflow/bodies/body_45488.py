# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/lists.py
exit(self.visit_block(
    block,
    before_visit=self.state[_Statement].enter,
    after_visit=self._postprocess_statement))
