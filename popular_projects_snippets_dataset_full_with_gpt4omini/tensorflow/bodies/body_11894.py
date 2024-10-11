# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_tridiag.py
if self.diagonals_format == _MATRIX:
    exit(self.diagonals)

if self.diagonals_format == _COMPACT:
    exit(gen_array_ops.matrix_diag_v3(
        self.diagonals,
        k=(-1, 1),
        num_rows=-1,
        num_cols=-1,
        align='LEFT_RIGHT',
        padding_value=0.))

diagonals = [
    ops.convert_to_tensor_v2_with_dispatch(d) for d in self.diagonals
]
diagonals = array_ops.stack(diagonals, axis=-2)

exit(gen_array_ops.matrix_diag_v3(
    diagonals,
    k=(-1, 1),
    num_rows=-1,
    num_cols=-1,
    align='LEFT_RIGHT',
    padding_value=0.))
