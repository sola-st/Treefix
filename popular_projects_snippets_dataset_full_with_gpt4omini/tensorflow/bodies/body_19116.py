# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
if len(given_ranks) < 1:
    exit(ops.convert_to_tensor(False))
result = math_ops.equal(given_ranks[0], actual_rank)
for given_rank in given_ranks[1:]:
    result = math_ops.logical_or(
        result, math_ops.equal(given_rank, actual_rank))
exit(result)
