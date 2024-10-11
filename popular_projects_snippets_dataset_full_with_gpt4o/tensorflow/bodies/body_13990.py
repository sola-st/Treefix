# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
for inp, out, loop_var in zip(body_graph.inputs, body_graph.outputs,
                              flattened_loop_vars):
    if inp.dtype != out.dtype:
        raise TypeError(
            f"Loop var {loop_var.name} enters the loop with type {inp.dtype} "
            f"but has type {out.dtype} after 1 iteration. {loop_var.name} type "
            "should remain constant.")
