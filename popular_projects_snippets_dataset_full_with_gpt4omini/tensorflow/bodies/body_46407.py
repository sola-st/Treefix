# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
exited_scope = self.scope
exited_scope.finalize()
self.scope = exited_scope.parent
exit(exited_scope)
