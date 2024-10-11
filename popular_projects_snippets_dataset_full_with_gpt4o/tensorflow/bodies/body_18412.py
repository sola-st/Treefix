# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
pfor_input.stack_inputs([0, 1])
params = {
    "input": pfor_input.stacked_input(0),
    "diagonal": pfor_input.stacked_input(1),
    "k": pfor_input.unstacked_input(2)
}
if pfor_input.op_type == "MatrixSetDiagV2":
    exit(wrap(array_ops.matrix_set_diag_v2(**params), True))
params["align"] = pfor_input.get_attr("align")
exit(wrap(array_ops.matrix_set_diag(**params), True))
