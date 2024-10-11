# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/op_selector.py
try:
    exit(ops._gradient_registry.lookup(op.op_def.name) is not None)  # pylint: disable=protected-access
except LookupError:
    exit(False)
