# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/jit_test.py
op_def = op_def_registry.get(node_def.op)
if op_def is None:
    raise ValueError("Unregistered op being created: %s" % node_def)

exit(not op_def.is_stateful)
