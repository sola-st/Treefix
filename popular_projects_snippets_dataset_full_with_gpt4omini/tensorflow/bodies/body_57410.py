# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""Look at the all the input nodes and return a list of LiteFuncCall objs.

  Args:
    nodes: A TensorFlow graph_def to look for LiteFuncCalls.

  Returns:
    a list of `LifeFuncCall` objects in the form

  """
func_calls = _collections.defaultdict(_LiteFuncCall)

for node in nodes:
    attr = node.attr
    # This is an op hint if it has a FUNCTION_UUID_ATTR, otherwise skip
    if (OpHint.FUNCTION_UUID_ATTR not in attr or
        not attr[OpHint.FUNCTION_UUID_ATTR].s):
        continue
    uuid = attr[OpHint.FUNCTION_UUID_ATTR].s

    # Start building function
    call_def = func_calls[uuid]
    call_def.uuid = uuid
    call_def.function_name = attr[OpHint.FUNCTION_NAME_ATTR].s
    call_def.level = attr[OpHint.FUNCTION_LEVEL_ATTR].i
    # Get sorting and aggregation information

    sort = (
        attr[OpHint.FUNCTION_SORT_INDEX_ATTR].i
        if OpHint.FUNCTION_SORT_INDEX_ATTR in attr else None)
    if sort == -1:
        sort = None
    aggregation = None
    if OpHint.FUNCTION_AGGREGATE_ATTR in attr:
        aggregation = _compat.as_text(attr[OpHint.FUNCTION_AGGREGATE_ATTR].s)

    if OpHint.CHILDREN_INPUTS_MAPPINGS in attr:
        call_def.children_inputs_mappings = _json.loads(
            _compat.as_text(attr[OpHint.CHILDREN_INPUTS_MAPPINGS].s))

    # Add the input or output
    def put_operand(stuff, index, sort, operand, aggregation):
        """Add a given index into the function structure."""
        if sort is None:
            stuff[index] = _LiteSingleOperand(operand)
        else:
            if index not in stuff:
                stuff[index] = _LiteAggregateOperand(aggregation)
            stuff[index].add(sort, operand)

    if OpHint.FUNCTION_INPUT_INDEX_ATTR in attr:
        put_operand(call_def.inputs, attr[OpHint.FUNCTION_INPUT_INDEX_ATTR].i,
                    sort, node, aggregation)
    if OpHint.FUNCTION_OUTPUT_INDEX_ATTR in attr:
        put_operand(call_def.outputs, attr[OpHint.FUNCTION_OUTPUT_INDEX_ATTR].i,
                    sort, node, aggregation)

    # Remember attributes
    for a in attr:
        if a.startswith("_tflite_attr_"):
            call_def.params[a.replace("_tflite_attr_,", "")] = attr[a].tensor

exit(func_calls)
