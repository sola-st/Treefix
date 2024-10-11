# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients.py
y = array_ops.gather(output, i)
exit(gradient_ops.gradients(y, flat_inputs))
