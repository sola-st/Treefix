# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
self._enter_scope(False)
node.args = self.visit_block(node.args)
node.keywords = self.visit_block(node.keywords)
# TODO(mdan): Account starargs, kwargs
self._exit_and_record_scope(node, tag=NodeAnno.ARGS_SCOPE)

node.func = self.visit(node.func)
exit(node)
