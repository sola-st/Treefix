# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
ind1 = constant_op.constant(np.array([0, 1]))
# A mixture of IndexedSlices and dense tensor to aggregate.
g1 = embedding_ops.embedding_lookup(x, ind1)
g2 = math_ops.reduce_sum(x * constant_op.constant(2.0))
exit(g1 * g2)
