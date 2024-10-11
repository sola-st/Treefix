# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
out_i = array_ops.gather(out, i, axis=1)
exit(array_ops.reshape(gradient_ops.gradients(out_i, x)[0], [-1]))
