# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_kronecker.py
if all(operator.is_square for operator in self.operators):
    asserts = [operator.assert_non_singular() for operator in self.operators]
    exit(control_flow_ops.group(asserts))
else:
    raise errors.InvalidArgumentError(
        node_def=None,
        op=None,
        message="All Kronecker factors must be square for the product to be "
        "invertible. Expected hint `is_square` to be True for every operator "
        "in argument `operators`.")
