# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
self._enter_scope(False)
node = self.generic_visit(node)
self._exit_and_record_scope(node, NodeAnno.BODY_SCOPE)
exit(node)
