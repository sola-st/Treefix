# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
scope = activity.Scope(None)
scope.read.add(QN('a'))

child = activity.Scope(scope)
child.read.add(QN('b'))

child2 = activity.Scope(child, isolated=False)
child2.read.add(QN('c'))

child2.finalize()
child.finalize()
scope.finalize()

self.assertIn(QN('c'), child2.referenced)
self.assertIn(QN('b'), child2.referenced)
self.assertIn(QN('a'), child2.referenced)

self.assertIn(QN('c'), child.referenced)
self.assertIn(QN('b'), child.referenced)
self.assertIn(QN('a'), child.referenced)
