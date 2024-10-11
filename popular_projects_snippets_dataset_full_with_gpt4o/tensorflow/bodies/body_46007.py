# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser_test.py
node, source = parser.parse_entity(lam, future_features=())
expected_node_src = 'lambda x: x'
self.assertAstMatches(node, expected_node_src)
self.assertMatchesWithPotentialGarbage(
    source, 'lambda x: x', ', named_arg=1)')
