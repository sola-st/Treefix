# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util_test.py
node = parser.parse('def f():\n  pass')
node = ast_util.rename_symbols(node,
                               {qual_names.QN('f'): qual_names.QN('f1')})

source = parser.unparse(node, include_encoding_marker=False)
self.assertEqual(source.strip(), 'def f1():\n    pass')
