# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
self._enter_scope(False)
# try/except oddity: as expected, it leaks any names you defined inside the
# except block, but not the name of the exception variable.
if node.name is not None:
    self.scope.isolated_names.add(anno.getanno(node.name, anno.Basic.QN))
node = self.generic_visit(node)
self._exit_scope()
exit(node)
