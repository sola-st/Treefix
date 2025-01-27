# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
template = 'foo = bar'
replacement = _parse_with_unset_ctx(expression_source)

target_node = templates.replace(template, foo=replacement)[0].targets[0]
self.assertExpectedCtxSet(target_node, gast.Store)

value_node = templates.replace(template, bar=replacement)[0].value
self.assertExpectedCtxSet(value_node, gast.Load)
