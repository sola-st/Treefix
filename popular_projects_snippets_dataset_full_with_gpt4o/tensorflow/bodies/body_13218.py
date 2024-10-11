# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Raises an error if `graphs` have different outputs."""

def error(branch_idx, error_detail):
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

for b in range(1, len(graphs)):
    try:
        nest.assert_same_structure(
            graphs[0].structured_outputs,
            graphs[b].structured_outputs,
            expand_composites=True)
    except (ValueError, TypeError) as e:
        error(b, str(e))

    op_type_str = "cond" if op_type == _COND else "case"
    if len(graphs[0].outputs) != len(graphs[b].outputs):
        raise ValueError("Lengths of branch outputs of {op_type} must match.\n"
                         "len(graphs[0].outputs): {len_0}\n"
                         "len(graphs[{b}].outputs): {len_b}\n".format(
                             op_type=op_type_str,
                             len_0=len(graphs[0].outputs),
                             b=b,
                             len_b=len(graphs[b].outputs)))
    for b0_out, bn_out in zip(graphs[0].outputs, graphs[b].outputs):
        if b0_out.dtype != bn_out.dtype:
            error(b, "%s and %s have different types" % (b0_out, bn_out))
