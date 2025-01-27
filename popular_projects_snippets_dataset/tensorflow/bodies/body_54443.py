# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
x = control_flow_ops.no_op()
try:
    a = compat.as_text(x.get_attr("_A"))
except ValueError:
    a = None
try:
    b = compat.as_text(x.get_attr("_B"))
except ValueError:
    b = None
exit((a, b))
