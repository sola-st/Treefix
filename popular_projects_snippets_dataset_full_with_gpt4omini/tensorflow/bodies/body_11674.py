# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py
for i, row in enumerate(self.operators):
    if len(row) != i + 1:
        raise ValueError(
            f"Argument `operators[{i}]` must contain `{i + 1}` blocks. "
            f"Received: {len(row)} blocks.")
