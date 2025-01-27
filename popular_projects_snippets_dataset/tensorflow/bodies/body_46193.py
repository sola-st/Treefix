# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util_test.py
node = parser.parse('a + b')
node = qual_names.resolve(node)

node = ast_util.rename_symbols(
    node, {qual_names.QN('a'): qual_names.QN('renamed_a')})
source = parser.unparse(node, include_encoding_marker=False)
expected_node_src = 'renamed_a + b'

self.assertIsInstance(node.value.left.id, str)
self.assertAstMatches(node, source)
self.assertAstMatches(node, expected_node_src)
