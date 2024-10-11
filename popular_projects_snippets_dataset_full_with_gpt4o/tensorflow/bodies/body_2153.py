# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/approx_topk_test.py
scores = math_ops.matmul(qy, db, transpose_b=True)
exit(nn_ops.approx_max_k(scores, k))
