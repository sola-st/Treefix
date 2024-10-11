# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared.py
"""Generate formatted str to represent a tensor or its slices.

  Args:
    tensor: (numpy ndarray) The tensor value.
    tensor_name: (str) Name of the tensor, e.g., the tensor's debug watch key.
    np_printoptions: (dict) Numpy tensor formatting options.
    print_all: (bool) Whether the tensor is to be displayed in its entirety,
      instead of printing ellipses, even if its number of elements exceeds
      the default numpy display threshold.
      (Note: Even if this is set to true, the screen output can still be cut
       off by the UI frontend if it consist of more lines than the frontend
       can handle.)
    tensor_slicing: (str or None) Slicing of the tensor, e.g., "[:, 1]". If
      None, no slicing will be performed on the tensor.
    highlight_options: (tensor_format.HighlightOptions) options to highlight
      elements of the tensor. See the doc of tensor_format.format_tensor()
      for more details.
    include_numeric_summary: Whether a text summary of the numeric values (if
      applicable) will be included.
    write_path: A path to save the tensor value (after any slicing) to
      (optional). `numpy.save()` is used to save the value.

  Returns:
    An instance of `debugger_cli_common.RichTextLines` representing the
    (potentially sliced) tensor.
  """

if tensor_slicing:
    # Validate the indexing.
    value = command_parser.evaluate_tensor_slice(tensor, tensor_slicing)
    sliced_name = tensor_name + tensor_slicing
else:
    value = tensor
    sliced_name = tensor_name

auxiliary_message = None
if write_path:
    with gfile.Open(write_path, "wb") as output_file:
        np.save(output_file, value)
    line = debugger_cli_common.RichLine("Saved value to: ")
    line += debugger_cli_common.RichLine(write_path, font_attr="bold")
    line += " (%sB)" % bytes_to_readable_str(gfile.Stat(write_path).length)
    auxiliary_message = debugger_cli_common.rich_text_lines_from_rich_line_list(
        [line, debugger_cli_common.RichLine("")])

if print_all:
    np_printoptions["threshold"] = value.size
else:
    np_printoptions["threshold"] = DEFAULT_NDARRAY_DISPLAY_THRESHOLD

exit(tensor_format.format_tensor(
    value,
    sliced_name,
    include_metadata=True,
    include_numeric_summary=include_numeric_summary,
    auxiliary_message=auxiliary_message,
    np_printoptions=np_printoptions,
    highlight_options=highlight_options))
