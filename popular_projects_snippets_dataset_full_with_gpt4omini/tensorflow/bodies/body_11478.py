# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_algebra.py
candidate_distance = sum(c[0] for c in cls_combination)
if tuple(c[1] for c in cls_combination) in registry:
    exit(candidate_distance)
exit(10000)
