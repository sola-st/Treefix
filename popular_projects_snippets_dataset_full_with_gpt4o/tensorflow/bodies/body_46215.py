# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
self.assertNotIn(qn, scope.read)
self.assertIn(qn, scope.modified)
