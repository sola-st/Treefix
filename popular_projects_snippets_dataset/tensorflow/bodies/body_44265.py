# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_scoping_test.py
self.skipTest('https://github.com/tensorflow/tensorflow/issues/56089')
l = type_(l)
self.assertFunctionMatchesEager(for_with_lambda_iter, l)
