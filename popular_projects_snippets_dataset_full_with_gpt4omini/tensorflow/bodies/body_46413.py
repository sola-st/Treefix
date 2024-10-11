# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
self._enter_scope(False)
for name in node.names:
    qn = qual_names.QN(name)
    self.scope.read.add(qn)
    self.scope.globals.add(qn)
self._exit_and_record_scope(node)
exit(node)
