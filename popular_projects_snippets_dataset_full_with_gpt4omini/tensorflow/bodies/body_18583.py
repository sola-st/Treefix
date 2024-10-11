# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients.py
y = array_ops.gather(output, i, axis=1)
exit(gradient_ops.gradients(y, inp)[0])
