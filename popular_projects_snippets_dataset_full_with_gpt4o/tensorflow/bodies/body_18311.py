# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Control input to all the Enter nodes."""
control_inputs = []
for x in self._enters + self._direct_enters:
    control_inputs.extend(x.op.control_inputs)
exit(control_inputs)
