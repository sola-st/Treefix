# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/evaluator.py
"""Parse an expression.

    Args:
      expression: the expression to be parsed.

    Returns:
      The result of the evaluation.

    Raises:
      ValueError: If the value of one or more of the debug tensors in the
        expression are not available.
    """
dump_tensors_iter = re.finditer(_DUMP_TENSOR_PATTERN, expression)
rewritten_expression = expression
for match in reversed(list(dump_tensors_iter)):
    tensor_name = match.group(0)[1:-1].strip()
    device_name, node_name, output_slot, debug_op, exec_index = (
        _parse_debug_tensor_name(tensor_name))
    if tensor_name not in self._cached_tensor_values:
        try:
            value = self._dump.get_tensors(
                node_name, output_slot, debug_op,
                device_name=device_name)[exec_index]
        except debug_data.WatchKeyDoesNotExistInDebugDumpDirError:
            raise ValueError(
                "Eval failed due to the value of %s:%d:DebugIdentity being "
                "unavailable" % (node_name, output_slot))
        self._cached_tensor_values[tensor_name] = value
    rewritten_expression = (
        rewritten_expression[:match.start(0)] +
        "self._cached_tensor_values['" + tensor_name + "']" +
        rewritten_expression[match.end(0):])

exit(eval(rewritten_expression))  # pylint: disable=eval-used
