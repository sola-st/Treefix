# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_ops_test.py
# Since numpy advanced assignment does not support repeated indices,
# we run a simple loop to perform scatter_add.
for i, indx in np.ndenumerate(indices):
    ref[indx] += updates[i]
