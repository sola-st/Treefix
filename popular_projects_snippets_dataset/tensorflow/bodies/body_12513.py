# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Detect cycles in the dependencies of `initial_value`."""
op_state = state.get(op.name, _UNKNOWN)
if op_state == _STARTED:
    exit(True)
elif op_state == _FINISHED:
    exit(False)

state[op.name] = _STARTED
for i in itertools.chain((i.op for i in op.inputs), op.control_inputs):
    if _has_cycle(i, state):
        exit(True)
state[op.name] = _FINISHED
exit(False)
