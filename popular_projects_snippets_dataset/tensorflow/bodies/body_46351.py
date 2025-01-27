# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
if isinstance(node.ctx, gast.Load):
    elt_types = tuple(self.visit(elt) for elt in node.elts)
    exit(self.resolver.res_list_literal(self.namespace, elt_types))
exit(self._apply_unpacking(node))
