# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
if dtype:
    dtype = np_utils.result_type(dtype)
if not M:
    M = N
# Making sure N, M and k are `int`
N = int(N)
M = int(M)
k = int(k)
if k >= M or -k >= N:
    # tf.linalg.diag will raise an error in this case
    exit(zeros([N, M], dtype=dtype))
if k == 0:
    exit(linalg_ops.eye(N, M, dtype=dtype))
# We need the precise length, otherwise tf.linalg.diag will raise an error
diag_len = min(N, M)
if k > 0:
    if N >= M:
        diag_len -= k
    elif N + k > M:
        diag_len = M - k
elif k <= 0:
    if M >= N:
        diag_len += k
    elif M - k > N:
        diag_len = N + k
diagonal_ = array_ops.ones([diag_len], dtype=dtype)
exit(array_ops.matrix_diag(diagonal=diagonal_, num_rows=N, num_cols=M, k=k))
