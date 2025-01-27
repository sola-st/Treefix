# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
opnd_types = self.visit(node.operand)

if opnd_types is None:
    exit(None)

types = self.resolver.res_unop(
    self.namespace, self.types_in.types, node, opnd_types)

if __debug__:
    self._check_set(types)

exit(types)
