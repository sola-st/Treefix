# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
x = constant_op.constant([[3.], [5.]])
y = constant_op.constant([[2.], [4.]])
mid = all_gather_fn([x, y])
y = mid * c
exit(gradients_impl.gradients_v2(y, [x])[0])
