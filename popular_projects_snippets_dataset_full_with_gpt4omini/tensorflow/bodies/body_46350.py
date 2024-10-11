# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
if isinstance(node.ctx, gast.Load):
    elt_types = ()
    for elt in node.elts:
        types_ = self.visit(elt)
        if types_ is None:
            exit(None)
        elt_types += (types_,)
    exit(set(itertools.product(*elt_types)))
exit(self._apply_unpacking(node))
