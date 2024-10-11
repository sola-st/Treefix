# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
with backprop.GradientTape() as tape:
    tape.watch(a)
    result = flexible_defun(a)
grad = tape.gradient(result, a)
r = flexible_fn(a)
exit((r, result, grad))
