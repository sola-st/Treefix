# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
out_i = array_ops.gather(out, i)
exit(gradient_ops.gradients(out_i, x)[0])
