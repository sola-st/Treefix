# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util_test.py
node = parser.parse('b.c = b.c.d')
node = qual_names.resolve(node)

node = ast_util.rename_symbols(
    node, {qual_names.from_str('b.c'): qual_names.QN('renamed_b_c')})

source = parser.unparse(node, include_encoding_marker=False)
self.assertEqual(source.strip(), 'renamed_b_c = renamed_b_c.d')
