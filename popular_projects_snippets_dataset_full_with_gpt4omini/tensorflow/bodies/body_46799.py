# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
template = """
        foo = bar
    """
replacement = qn.QN(qn.QN('dictionary'), subscript=qn.QN('key'))

node = templates.replace(template, foo=replacement)[0].targets[0]
self.assertIsInstance(node.ctx, gast.Store)
self.assertIsInstance(node.value.ctx, gast.Load)
