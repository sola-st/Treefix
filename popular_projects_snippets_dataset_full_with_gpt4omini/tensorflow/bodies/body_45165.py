# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/directives.py
node = self.generic_visit(node)
if isinstance(node.ctx, gast.Load):
    defs = anno.getanno(node, anno.Static.DEFINITIONS, ())
    is_defined = bool(defs)
    if not is_defined and node.id in self.ctx.info.namespace:
        anno.setanno(node, STATIC_VALUE, self.ctx.info.namespace[node.id])
exit(node)
