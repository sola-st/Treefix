# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
# This is a somewhat convoluted way of testing that nothing gets added to
# a global collection.
predictions = constant_op.constant([4, 8, 12, 8, 1, 3], shape=(2, 3))
labels = constant_op.constant([1, 9, 2, -5, -2, 6], shape=(2, 3))
losses.absolute_difference(labels, predictions)
