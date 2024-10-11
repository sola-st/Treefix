# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util_test.py
self.assertEqual(len(matching_nodes), len(expected_bodies))
for node in matching_nodes:
    self.assertIsInstance(node, gast.Lambda)
    self.assertIn(
        parser.unparse(node.body, include_encoding_marker=False).strip(),
        expected_bodies)
