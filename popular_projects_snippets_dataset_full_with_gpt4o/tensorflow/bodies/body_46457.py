# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py
actual = anno.getanno(node, anno.Static.CLOSURE_TYPES)
actual = {str(k): v for k, v in actual.items()}
for k, v in expected.items():
    self.assertIn(k, actual)
    self.assertEqual(actual[k], v)
