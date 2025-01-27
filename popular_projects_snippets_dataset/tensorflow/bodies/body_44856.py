# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/converter_testing.py
node = self.initial_analysis(node, ctx)

for c in self._converters:
    node = c.transform(node, ctx)

self.transformed_ast = node
self.transform_ctx = ctx
exit(node)
