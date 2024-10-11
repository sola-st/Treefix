# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser_test.py

_ = lambda x: x + 1
l = lambda x: x + 1
_ = lambda x: x + 1
expected_node_src = 'lambda x: (x + 1)'

node, source = parser.parse_entity(l, future_features=())
self.assertAstMatches(node, source)
self.assertAstMatches(node, expected_node_src)
self.assertEqual(source, 'lambda x: x + 1')
