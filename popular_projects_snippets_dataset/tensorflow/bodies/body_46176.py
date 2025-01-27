# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
# TODO(mdan): Mark the context manager's exit call as exit guard.
for item in node.items:
    self._process_basic_statement(item)
for stmt in node.body:
    self.visit(stmt)
