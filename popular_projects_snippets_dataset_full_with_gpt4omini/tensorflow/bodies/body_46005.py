# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser_test.py

l = (
    lambda x: lambda y: x + y + 1,
    lambda x: lambda y: x + y + 2,
    )

node, source = parser.parse_entity(l[0], future_features=())
expected_node_src = 'lambda x: (lambda y: ((x + y) + 1))'
self.assertAstMatches(node, expected_node_src)
self.assertMatchesWithPotentialGarbage(
    source, 'lambda x: lambda y: x + y + 1', ',')

node, source = parser.parse_entity(l[0](0), future_features=())
expected_node_src = 'lambda y: ((x + y) + 1)'
self.assertAstMatches(node, expected_node_src)
self.assertMatchesWithPotentialGarbage(
    source, 'lambda y: x + y + 1', ',')

node, source = parser.parse_entity(l[1], future_features=())
expected_node_src = 'lambda x: (lambda y: ((x + y) + 2))'
self.assertAstMatches(node, expected_node_src)
self.assertMatchesWithPotentialGarbage(source,
                                       'lambda x: lambda y: x + y + 2', ',')

node, source = parser.parse_entity(l[1](0), future_features=())
expected_node_src = 'lambda y: ((x + y) + 2)'
self.assertAstMatches(node, expected_node_src)
self.assertMatchesWithPotentialGarbage(source, 'lambda y: x + y + 2', ',')
