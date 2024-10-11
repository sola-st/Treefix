# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
x = constant_op.constant([[3.], [5.]])
mid = all_gather_fn(x)
y = mid * c
exit(gradients_impl.gradients_v2(y, [x])[0])
