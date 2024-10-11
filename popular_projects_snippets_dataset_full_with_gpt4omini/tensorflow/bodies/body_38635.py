# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/approx_topk_test.py
scores = math_ops.matmul(qy, db, transpose_b=True)
exit(nn_ops.approx_max_k(scores, k))
