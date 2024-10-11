# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_ops_test.py
for _, indx in np.ndenumerate(indices):
    ref[indx] = np.maximum(ref[indx], update)
