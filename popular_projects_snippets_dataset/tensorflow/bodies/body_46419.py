# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
self._enter_scope(False)
node.target = self.visit(node.target)
if node.value is not None:
    # Can be None for pure declarations, e.g. `n: int`. This is a new thing
    # enabled by type annotations, but does not influence static analysis
    # (declarations are not definitions).
    node.value = self.visit(node.value)
if node.annotation:
    node.annotation = self._process_annotation(node.annotation)
self._exit_and_record_scope(node)
exit(node)
