# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
left_types = self.visit(node.left)
right_types = self.visit(node.right)

if left_types is None or right_types is None:
    exit(None)

types = self.resolver.res_binop(
    self.namespace, self.types_in.types, node, left_types, right_types)

if __debug__:
    self._check_set(types)

exit(types)
