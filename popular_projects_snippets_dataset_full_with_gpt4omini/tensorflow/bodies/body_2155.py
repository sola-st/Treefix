# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/approx_topk_test.py
scores = db_half_norm_sq - math_ops.matmul(qy, db, transpose_b=True)
exit(nn_ops.approx_min_k(scores, k))
