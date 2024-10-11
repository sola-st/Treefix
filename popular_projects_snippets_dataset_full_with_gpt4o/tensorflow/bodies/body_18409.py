# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
params = {
    "diagonal": pfor_input.stacked_input(0),
    "k": pfor_input.unstacked_input(1),
    "num_rows": pfor_input.unstacked_input(2),
    "num_cols": pfor_input.unstacked_input(3),
    "padding_value": pfor_input.unstacked_input(4)
}
if pfor_input.op_type == "MatrixDiagV2":
    exit(wrap(array_ops.matrix_diag_v2(**params), True))
params["align"] = pfor_input.get_attr("align")
exit(wrap(array_ops.matrix_diag(**params), True))
