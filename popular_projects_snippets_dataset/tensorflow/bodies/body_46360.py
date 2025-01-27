# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
val_types = self.visit(node.value)
slice_types = self.visit(node.slice)

if val_types is None or slice_types is None:
    exit(None)

types = self.resolver.res_slice(
    self.namespace, self.types_in.types, node, val_types, slice_types)

if __debug__:
    self._check_set(types)

exit(types)
