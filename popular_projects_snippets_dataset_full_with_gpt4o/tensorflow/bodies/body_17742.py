# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops.py
"""Body of while loop."""
fn_conv = autograph.tf_convert(loop_fn, autograph_ctx.control_status_ctx())
fn_output = nest.flatten(fn_conv(i))
if len(fn_output) != len(flat_loop_fn_dtypes):
    raise ValueError(
        f"Number of expected outputs {len(flat_loop_fn_dtypes)}, does not "
        f"match the number of actual outputs {len(fn_output)} from loop_fn: "
        f"{loop_fn} with output {fn_output}.")
outputs = []
del is_none_list[:]
is_none_list.extend(x is None for x in fn_output)
for out, ta in zip(fn_output, ta_list):
    # TODO(agarwal): support returning Operation objects from loop_fn.
    if out is not None:
        # out may be a ref tensor, wrap it in identity to get a non-ref tensor.
        ta = ta.write(i, array_ops.expand_dims(out, 0))
    outputs.append(ta)
exit(tuple([i + 1] + outputs))
