# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
self._enter_scope(False)
node.values = self.visit_block(node.values)
node_scope = self._exit_and_record_scope(node)
anno.setanno(node, NodeAnno.ARGS_SCOPE, node_scope)
exit(node)
