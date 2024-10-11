# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/anno_test.py
node_1 = ast.Name()
anno.setanno(node_1, 'foo', 3)

node_2 = ast.Name()
anno.copyanno(node_1, node_2, 'foo')
anno.copyanno(node_1, node_2, 'bar')

self.assertTrue(anno.hasanno(node_2, 'foo'))
self.assertFalse(anno.hasanno(node_2, 'bar'))
