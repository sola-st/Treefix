# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
y_i = array_ops.gather(y, i)
grad = gradient_ops.gradients(y_i, x)[0]
exit(array_ops.gather(grad, i))
