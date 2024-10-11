# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util_test.py
node = parser.parse('global a, b, c')
node = qual_names.resolve(node)

node = ast_util.rename_symbols(
    node, {qual_names.from_str('b'): qual_names.QN('renamed_b')})

source = parser.unparse(node, include_encoding_marker=False)
self.assertEqual(source.strip(), 'global a, renamed_b, c')
