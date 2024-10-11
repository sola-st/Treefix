# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape_test.py
mm, r = two_outputs(x, y)
exit(r + math_ops.reduce_sum(mm))
