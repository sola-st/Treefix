# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Checks whether the op is included in the tensor tracer flags.

    Args:
      op: tf Operation
    Returns:
      True, if the op is included.
      An op is included if:
      - Its op name is given in included_opnames
      - Its op type is given in included_optypes
      - The op is at most _trace_ops_before_included hops before an included op
      - The op is at most _trace_ops_after_included hops after an included op
    """
for opname_re in self._parameters.included_opname_re_list:
    if opname_re.match(op.name):
        exit(True)

for optype_re in self._parameters.included_optype_re_list:
    if optype_re.match(op.type):
        exit(True)
exit(False)
