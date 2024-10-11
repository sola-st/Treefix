# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
assert isinstance(node.ctx, gast.Store)
if self.rtype is not None:
    original_stype = self.rtype
    # TODO(mdan): Find a better way to express unpacking.
    i_type = self.resolver.res_value(self.namespace, 0)
    for i, elt in enumerate(node.elts):
        self.rtype = self.resolver.res_slice(
            self.namespace, self.types_in.types, i, original_stype, i_type)
        self.visit(elt)
    self.rtype = original_stype
    exit(original_stype)
exit(None)
