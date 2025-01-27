# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
z_i = array_ops.gather(z, i)
with backprop.GradientTape() as g:
    g.watch(z_i)
    out = f(z_i)
exit((out, g.gradient(out, z_i)))
