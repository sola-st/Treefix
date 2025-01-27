# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
out_i = array_ops.gather(out, i, axis=1)
grad = gradient_ops.gradients(out_i, x)
exit(array_ops.reshape(grad[0], [-1]))
