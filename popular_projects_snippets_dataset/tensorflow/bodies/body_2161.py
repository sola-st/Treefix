# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/approx_topk_test.py
result1 = nn_ops.approx_max_k(db1, k, aggregate_to_topk=True)
result2 = nn_ops.approx_max_k(db2, k, aggregate_to_topk=True)
exit((result1, result2))
