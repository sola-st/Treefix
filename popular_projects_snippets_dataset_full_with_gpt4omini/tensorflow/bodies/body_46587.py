# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py
test_self.assertIn(node_or_slice, (0, 1))
test_self.assertSetEqual(value, {(int, float)})
test_self.assertEqual(slice_, int)
exit({t[node_or_slice] for t in value})
