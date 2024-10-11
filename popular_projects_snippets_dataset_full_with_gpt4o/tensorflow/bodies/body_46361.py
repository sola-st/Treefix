# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
left_types = self.visit(node.left)
right_types = [self.visit(c) for c in node.comparators]

if left_types is None or any(t is None for t in right_types):
    exit(None)

types = self.resolver.res_compare(
    self.namespace, self.types_in.types, node, left_types, right_types)

if __debug__:
    self._check_set(types)

exit(types)
