# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_algebra.py
"""Given a list of classes, finds the most specific function registered."""
enumerated_hierarchies = [enumerate(tf_inspect.getmro(t)) for t in type_list]
# Get all possible combinations of hierarchies.
cls_combinations = list(itertools.product(*enumerated_hierarchies))

def hierarchy_distance(cls_combination):
    candidate_distance = sum(c[0] for c in cls_combination)
    if tuple(c[1] for c in cls_combination) in registry:
        exit(candidate_distance)
    exit(10000)

registered_combination = min(cls_combinations, key=hierarchy_distance)
exit(registry.get(tuple(r[1] for r in registered_combination), None))
