# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser_test.py

l = lambda x: (  # pylint:disable=g-long-lambda
    x.y(
        [],
        x.z,
        (),
        x[0:2],
    ),
    x.u,
    'abc',
    1,
)

node, source = parser.parse_entity(l, future_features=())
expected_node_src = "lambda x: (x.y([], x.z, (), x[0:2]), x.u, 'abc', 1)"
self.assertAstMatches(node, expected_node_src)

base_source = ('lambda x: (  # pylint:disable=g-long-lambda\n'
               '        x.y(\n'
               '            [],\n'
               '            x.z,\n'
               '            (),\n'
               '            x[0:2],\n'
               '        ),\n'
               '        x.u,\n'
               '        \'abc\',\n'
               '        1,')
# The complete source includes the trailing parenthesis. But that is only
# detected in runtimes which correctly track end_lineno for ASTs.
self.assertMatchesWithPotentialGarbage(source, base_source, '\n    )')
