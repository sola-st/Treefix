# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
moments = [0.0] * (max_moment + 1)
for k in range(len(moments)):
    moments[k] = np.mean(samples**k, axis=0)
exit(moments)
