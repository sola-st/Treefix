# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
scope = activity.Scope(None)
scope.modified.add(QN('foo'))
other = activity.Scope(None)
other.copy_from(scope)

self.assertWriteOnly(QN('foo'), other)

scope.modified.add(QN('bar'))
scope.copy_from(other)

self.assertMissing(QN('bar'), scope)
