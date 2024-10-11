# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/input_lib.py
init_ops = []
for it in self._iterators:
    init_ops.extend(it.initialize())
exit(control_flow_ops.group(init_ops))
