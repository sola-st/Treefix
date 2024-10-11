# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback.py
"""Create a meaningful and user-friendly error message about offending tensor.

  The error message reveals the following info about the op that outputs
  NaN/Infinity: dtype, shape (to the extent known at graph-construction time),
  input tensors, stack trace for op creation (if is graph mode).

  Args:
    slot: (int) slot index of the tensor output.
    num_outputs: (int) total number of outputs of the op.
    op_type: (str) Type of the that generates `tensor`.
    tensor: (Tensor) the offending tensor, i.e., the tensor that contains
      Infinities or NaNs.
    inputs: (array of Tensor) inputs to the op that generates `tensor`.
    graph: (tf.Graph) the graph object that `tensor` belongs to. Available only
      under graph mode.
    traceback: (list of trace frames) the stack trace of the op's creation.
      Available only under graph model.
    stack_height_limit: (int or None) If int, limit to the height of the stack
      trace printed in the error message. If None, no limit to the height.
    path_length_limit: (int or None) Length limit for file paths included in the
      formatted stack trace.

  Returns:
    (str) A formatted error message.
  """
eager_vs_graph_qualifier = "graph" if graph else "eagerly-executing"
message = "\n"
message += (
    "\n!!! Detected Infinity or NaN in output %d of "
    "%s op \"%s\" (# of outputs: %d) !!!\n" %
    (slot, eager_vs_graph_qualifier, op_type, num_outputs))

message += "  dtype: %s\n" % tensor.dtype
message += "  shape: %s\n" % (tensor.shape,)

if not graph:
    # This is an eager tensor. We can get its numpy value and count
    # NaNs and Infs.
    is_inf = np.isinf(tensor)

    num_neg_inf = np.sum(np.logical_and(np.less(tensor, 0.), is_inf))
    num_pos_inf = np.sum(np.logical_and(np.greater(tensor, 0.), is_inf))
    num_nan = np.sum(np.isnan(tensor))
    if num_neg_inf > 0:
        message += "  # of -Inf elements: %s\n" % num_neg_inf
    if num_pos_inf > 0:
        message += "  # of +Inf elements: %s\n" % num_pos_inf
    if num_nan:
        message += "  # of +NaN elements: %s\n" % num_nan

if len(inputs) > 1:
    message += "\n  Input tensors (%d):\n" % len(inputs)
    for slot, input_tensor in enumerate(inputs):
        message += "         %d: %s\n" % (
            slot, _maybe_lookup_original_input_tensor(graph, input_tensor))
elif len(inputs) == 1:
    message += "\n  Input tensor: %s\n" % (
        _maybe_lookup_original_input_tensor(graph, inputs[0]))
if graph and hasattr(graph, "name") and graph.name:
    message += "  Graph name: \"%s\"\n" % graph.name

# Format the stack trace for the op's creation. We omit files that
# belong to tensorflow itself.
if graph and traceback:
    message += (
        "\n  Stack trace of op's creation (\"->\": inferred user code):\n")
    if stack_height_limit is not None and len(traceback) > stack_height_limit:
        num_omitted_frames = len(traceback) - stack_height_limit
        message += "    + ... (Omitted %d frames)\n" % num_omitted_frames
    for filepath, lineno, function_name, source_line in traceback[
        -stack_height_limit:]:
        user_code_indicator = "    "
        if not source_utils.guess_is_tensorflow_py_library(filepath):
            user_code_indicator = " -> "

        message += "    + %s (L%d) %s\n" % (
            limit_string_length(filepath, path_length_limit), lineno,
            function_name)
        if source_line is not None:
            message += "%s|   %s\n" % (user_code_indicator, source_line)
message += "\n"
exit(message)
