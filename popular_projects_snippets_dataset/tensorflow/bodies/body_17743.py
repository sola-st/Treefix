# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops.py
"""Runs `loop_fn` `iters` times and stacks the outputs.


  Runs `loop_fn` `iters` times, with input values from 0 to `iters - 1`, and
  stacks corresponding outputs of the different runs.

  Args:
    loop_fn: A function that takes an int32 scalar tf.Tensor object representing
      the iteration number, and returns a possibly nested structure of tensor
      objects. The shape of these outputs should not depend on the input.
    loop_fn_dtypes: dtypes for the outputs of `loop_fn`.
    iters: Number of iterations for which to run `loop_fn`.
    parallel_iterations: The number of iterations that can be dispatched in
      parallel. This knob can be used to control the total memory usage.

  Returns:
    Returns a nested structure of stacked output tensor objects with the same
    nested structure as the output of `loop_fn`.
  """

flat_loop_fn_dtypes = nest.flatten(loop_fn_dtypes)
is_none_list = []

def while_body(i, *ta_list):
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

if parallel_iterations is not None:
    extra_args = {"parallel_iterations": parallel_iterations}
else:
    extra_args = {}
ta_list = control_flow_ops.while_loop(
    lambda i, *ta: i < iters,
    while_body,
    [0] + [tensor_array_ops.TensorArray(dtype.base_dtype, iters)
           for dtype in flat_loop_fn_dtypes],
    **extra_args)[1:]

# TODO(rachelim): enable this for sparse tensors

output = [None if is_none else ta.concat()
          for ta, is_none in zip(ta_list, is_none_list)]
assert len(output) in (0, len(flat_loop_fn_dtypes))
if not output:
    # This may happen for the case where iters == 0.
    exit(None)
else:
    exit(nest.pack_sequence_as(loop_fn_dtypes, output))
