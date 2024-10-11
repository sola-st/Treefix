# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py
for i, row in enumerate(self.operators):
    for operator in row:
        if operator.dtype != dtype:
            name_type = (str((o.name, o.dtype)) for o in row)
            raise TypeError(
                "Expected all operators to have the same dtype.  Found {} in row "
                "{} and {} in row 0.".format(name_type, i, str(dtype)))
