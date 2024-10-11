# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py
"""Check that `operators` have compatible dimensions."""
for i in range(1, len(self.operators)):
    for j in range(i):
        op = self.operators[i][j]

        # `above_op` is the operator directly above `op` in the blockwise
        # structure, in row partition `i-1`, column partition `j`. `op` should
        # have the same `domain_dimension` as `above_op`.
        above_op = self.operators[i - 1][j]

        # `right_op` is the operator to the right of `op` in the blockwise
        # structure, in row partition `i`, column partition `j+1`. `op` should
        # have the same `range_dimension` as `right_op`.
        right_op = self.operators[i][j + 1]

        if (op.domain_dimension is not None and
            above_op.domain_dimension is not None):
            if op.domain_dimension != above_op.domain_dimension:
                raise ValueError(f"Argument `operators[{i}][{j}].domain_dimension` "
                                 f"({op.domain_dimension}) must be the same as "
                                 f"`operators[{i-1}][{j}].domain_dimension` "
                                 f"({above_op.domain_dimension}).")
        if (op.range_dimension is not None and
            right_op.range_dimension is not None):
            if op.range_dimension != right_op.range_dimension:
                raise ValueError(f"Argument `operators[{i}][{j}].range_dimension` "
                                 f"({op.range_dimension}) must be the same as "
                                 f"`operators[{i}][{j + 1}].range_dimension` "
                                 f"({right_op.range_dimension}).")
