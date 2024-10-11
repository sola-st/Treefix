# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
self._enter_scope(False)
block = self.visit_block(block)
self._exit_and_record_scope(node, tag=scope_name)
exit(node)
