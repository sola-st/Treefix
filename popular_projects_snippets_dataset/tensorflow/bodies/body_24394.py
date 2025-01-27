# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
new_u = state_ops.assign_add(u, v)
new_i = math_ops.add(i, 1)
op = control_flow_ops.group(new_u)
new_i = control_flow_ops.with_dependencies([op], new_i)
exit([new_i])
