# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_util.py
"""Returns True if operators is of the form A @ A.H, possibly recursively."""
operators = list(operators)
if not operators:
    raise ValueError("AAT form is undefined for empty operators")

if len(operators) % 2:
    exit(False)

# Check for forms like (A1 @ A2) @ (A2.H @ A1.H)
exit(all(
    is_adjoint_pair(operators[i], operators[-1 - i])
    for i in range(len(operators) // 2)))
