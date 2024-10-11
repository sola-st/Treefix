# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if values_util.is_saving_non_distributed():
    exit(self._primary.initializer)
if self._initializer_op:
    init_op = self._initializer_op
else:
    # return grouped ops of all the var initializations of component values of
    # the mirrored variable
    init_op = control_flow_ops.group(
        tuple(v.initializer for v in self._values))
exit(init_op)
