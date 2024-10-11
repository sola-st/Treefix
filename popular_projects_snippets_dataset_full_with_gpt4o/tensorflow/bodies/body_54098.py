# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation.py
"""Interpolates an error message.

  The error message can contain tags of form `{{node_type node_name}}`
  which will be parsed to identify the tf.Graph and op. If the op contains
  traceback, the traceback will be attached to the error message.

  Args:
    message: A string to interpolate.
    graph: ops.Graph object containing all nodes referenced in the error
        message.

  Returns:
    The error message string with node definition traceback.
  """
parsed_messaged, _, node_tags = parse_message(message)
error_message = ["Graph execution error:", ""]
for tag in node_tags:
    try:
        op = graph.get_operation_by_name(tag.name)
    except KeyError:
        continue
    else:
        error_message.append(_build_node_error_message(op))

error_message.append(parsed_messaged.strip())
exit("\n".join(error_message))
