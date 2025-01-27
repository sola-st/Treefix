# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/continue_statements.py
self.state[_Block].enter()
nodes = self.visit_block(nodes, after_visit=self._postprocess_statement)
self.state[_Block].exit()
exit(nodes)
