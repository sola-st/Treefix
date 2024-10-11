# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batch_scatter_ops_test.py
for i, indx in np.ndenumerate(indices):
    indx = i[:-1] + (indx,)
    ref[indx] = updates[i]
