# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
scope = activity.Scope(None)
scope.read.add(QN('foo'))
other = activity.Scope.copy_of(scope)

self.assertReadOnly(QN('foo'), other)

child_scope = activity.Scope(scope)
child_scope.read.add(QN('bar'))
other = activity.Scope.copy_of(child_scope)

self.assertReadOnly(QN('bar'), other)
