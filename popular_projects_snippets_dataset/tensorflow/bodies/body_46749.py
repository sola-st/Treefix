# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/anno_test.py
node = ast.If(
    test=ast.Num(1),
    body=[ast.Expr(ast.Name('bar', ast.Load()))],
    orelse=[])
anno.setanno(node, 'spam', 1)
anno.setanno(node, 'ham', 1)
anno.setanno(node.body[0], 'ham', 1)

anno.dup(node, {'spam': 'eggs'})

self.assertTrue(anno.hasanno(node, 'spam'))
self.assertTrue(anno.hasanno(node, 'ham'))
self.assertTrue(anno.hasanno(node, 'eggs'))
self.assertFalse(anno.hasanno(node.body[0], 'eggs'))
