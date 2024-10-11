# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
name = self.op_type
assert name not in _pfor_converter_registry, "Re-registering %s " % name
_pfor_converter_registry[name] = converter
exit(converter)
