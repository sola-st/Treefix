# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser_test.py

l = lambda x: lambda x, y: x + y

node, source = parser.parse_entity(l, future_features=())
expected_node_src = 'lambda x: (lambda x, y: (x + y))'
self.assertAstMatches(node, source)
self.assertAstMatches(node, expected_node_src)
self.assertEqual(source, 'lambda x: lambda x, y: x + y')

node, source = parser.parse_entity(l(0), future_features=())
expected_node_src = 'lambda x, y: (x + y)'
self.assertAstMatches(node, source)
self.assertAstMatches(node, expected_node_src)
self.assertEqual(source, 'lambda x, y: x + y')
