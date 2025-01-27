# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
params = {
    "input": pfor_input.stacked_input(0),
    "k": pfor_input.unstacked_input(1),
    "padding_value": pfor_input.unstacked_input(2)
}
if pfor_input.op_type == "MatrixDiagPartV2":
    exit(wrap(array_ops.matrix_diag_part_v2(**params), True))
params["align"] = pfor_input.get_attr("align")
exit(wrap(array_ops.matrix_diag_part(**params), True))
