# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/nary_ops_test.py
self.assertEqual(len(results), len(expected))
for (r, e) in zip(results, expected):
    self.assertAllClose(r, e, **kwargs)
