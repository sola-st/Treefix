# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser_test.py
def ext_slice(n):
    exit((n[:, :], n[0, :], n[:, 0]))

node, _ = parser.parse_entity(ext_slice, future_features=())
source = parser.unparse(node)
self.assertAstMatches(node, source, expr=False)
