# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
x = array_ops.identity(42.)
y = comm_fn(x) * c
exit(gradients_impl.gradients(y, [x])[0])
