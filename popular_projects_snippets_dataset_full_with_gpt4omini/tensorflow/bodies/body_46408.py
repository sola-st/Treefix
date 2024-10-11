# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
node_scope = self._exit_scope()
anno.setanno(node, tag, node_scope)
exit(node_scope)
