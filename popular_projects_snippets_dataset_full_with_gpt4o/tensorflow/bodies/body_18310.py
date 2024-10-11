# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Input to all the Enter nodes."""
exit([x.op.inputs[0] for x in self._enters + self._direct_enters])
