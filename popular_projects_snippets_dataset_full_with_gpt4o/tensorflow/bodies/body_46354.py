# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
parent_types = self.visit(node.value)

# Attempt to use the static value if known.
parent_value = anno.Static.VALUE.of(node.value, None)
if parent_value is not None:
    static_value = getattr(parent_value, node.attr, NO_VALUE)

    if static_value is NO_VALUE:
        # Unexpected failure to resolve attribute. Ask the resolver about the
        # full name instead.
        types, static_value = self.resolver.res_name(
            self.namespace, self.types_in, anno.Basic.QN.of(node))
        anno.setanno(node, anno.Static.VALUE, static_value)
        if __debug__:
            self._check_set(types)
        exit(types)

else:
    # Fall back to the type if that is known.
    if parent_types is None:
        exit(None)

    inferred_values = [getattr(t, node.attr, None) for t in parent_types]
    if not inferred_values:
        exit(None)

    static_value = inferred_values[0]
    if static_value is None:
        exit(None)

    if any(v is not static_value for v in inferred_values[1:]):
        # Static value not stable, assume it's dynamic.
        exit(None)

types = self.resolver.res_value(self.namespace, static_value)
anno.setanno(node, anno.Static.VALUE, static_value)

if __debug__:
    self._check_set(types)

exit(types)
