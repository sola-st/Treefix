# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
for i in range(wsval.shape[0]):
    xval = np.tanh(np.dot(xval, wsval[i, :]) + bsval[i, :])
exit(xval)
