# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/anno_test.py
node = ast.Name()

self.assertEqual(anno.keys(node), set())
self.assertFalse(anno.hasanno(node, 'foo'))
with self.assertRaises(AttributeError):
    anno.getanno(node, 'foo')

anno.setanno(node, 'foo', 3)

self.assertEqual(anno.keys(node), {'foo'})
self.assertTrue(anno.hasanno(node, 'foo'))
self.assertEqual(anno.getanno(node, 'foo'), 3)
self.assertEqual(anno.getanno(node, 'bar', default=7), 7)

anno.delanno(node, 'foo')

self.assertEqual(anno.keys(node), set())
self.assertFalse(anno.hasanno(node, 'foo'))
with self.assertRaises(AttributeError):
    anno.getanno(node, 'foo')
self.assertIsNone(anno.getanno(node, 'foo', default=None))
