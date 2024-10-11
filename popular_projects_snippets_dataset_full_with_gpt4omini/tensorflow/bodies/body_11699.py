# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py
# None of the operators contribute to the matrix shape.
exit({"operators": nest.map_structure(lambda _: 0, self.operators)})
