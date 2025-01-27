# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/softmax_op_test.py
if dim == -1:
    dim = len(features.shape) - 1
one_only_on_dim = list(features.shape)
one_only_on_dim[dim] = 1
is_fp16 = features.dtype == np.float16
if is_fp16:
    # Do the compute in fp32 and cast the input back to fp32.
    features = features.astype(np.float32)
e = np.exp(features - np.reshape(
    np.amax(
        features, axis=dim), one_only_on_dim))
softmax = e / np.reshape(np.sum(e, axis=dim), one_only_on_dim)
if log:
    res = np.log(softmax)
else:
    res = softmax
if is_fp16:
    res = res.astype(np.float16)
exit(res)
