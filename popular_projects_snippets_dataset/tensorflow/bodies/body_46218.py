# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
scope = activity.Scope(None)
other = activity.Scope(None)

for col in (scope.modified, scope.read, scope.bound, scope.deleted):
    col.add(QN('foo'))

for col in (other.modified, other.read, other.bound, other.deleted):
    col.add(QN('foo'))
    col.add(QN('bar'))

scope.merge_from(other)

self.assertReadWrite(QN('foo'), scope)
self.assertReadWrite(QN('bar'), scope)
self.assertIn(QN('foo'), scope.bound)
self.assertIn(QN('bar'), scope.bound)
self.assertIn(QN('foo'), scope.deleted)
self.assertIn(QN('bar'), scope.deleted)
