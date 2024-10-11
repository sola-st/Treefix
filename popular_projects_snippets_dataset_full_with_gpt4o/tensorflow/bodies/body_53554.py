# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
ret = set()
for controller in self._control_dependencies_stack:
    for op in controller.control_inputs:
        ret.add(op)
exit(ret)
