# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
raise TypeError(
    "{b0_name} and {bn_name} arguments to {op_name} must have the same "
    "number, type, and overall structure of return values.\n"
    "\n"
    "{b0_name} output: {b0_out}\n"
    "{bn_name} output: {bn_out}\n"
    "\n"
    "Error details:\n"
    "{detail}".format(
        b0_name="true_fn" if op_type == _COND else "branches[0]",
        bn_name=("false_fn" if op_type == _COND else
                 "branches[{}]".format(branch_idx)),
        op_name="tf.cond" if op_type == _COND else "tf.switch_case",
        b0_out=graphs[0].structured_outputs,
        bn_out=graphs[branch_idx].structured_outputs,
        detail=error_detail))
