# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser_test.py

lambda_lam = lambda x: x + 1
expected_node_src = 'lambda x: (x + 1)'

node, source = parser.parse_entity(lambda_lam, future_features=())
self.assertAstMatches(node, source)
self.assertAstMatches(node, expected_node_src)
