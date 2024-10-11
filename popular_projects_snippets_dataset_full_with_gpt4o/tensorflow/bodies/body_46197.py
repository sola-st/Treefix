# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util_test.py
node = parser.parse('a[i]')
node = qual_names.resolve(node)
anno.setanno(node, 'foo', 'bar')
orig_anno = anno.getanno(node, 'foo')

node = ast_util.rename_symbols(node,
                               {qual_names.QN('a'): qual_names.QN('b')})

self.assertIs(anno.getanno(node, 'foo'), orig_anno)
