# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
x, mask = inputs
y = x * mask
exit(math_ops.reduce_sum(y))
