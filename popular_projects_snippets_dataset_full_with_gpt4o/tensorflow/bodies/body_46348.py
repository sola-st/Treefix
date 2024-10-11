# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
types = self.resolver.res_value(self.namespace, node.value)
if __debug__:
    self._check_set(types)
exit(types)
