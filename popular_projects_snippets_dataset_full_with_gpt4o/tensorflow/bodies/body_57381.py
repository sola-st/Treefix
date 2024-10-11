# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""Return a wrapped tensor of an input tensor as an argument.

      Args:
        arg: A TensorFlow tensor that should be considered an argument.
        tag: String tag to identify arguments that should be packed.
        name: Name of argument. This is included in the Identity hint op names.
        aggregate: Strategy to aggregate.
        Acceptable values are OpHint.AGGREGATE_FIRST, OpHint.AGGREGATE_LAST,
          and OpHint.AGGREGATE_STACK.
          Note, aggregate is only valid if tag is specified.
        index_override: Specify what input/output index should this be in the
          final stub. i.e. add(arg0, index=1); add(arg1, index=0) will make the
          final stub be as stub_func(inputs[arg1, arg0], outputs=[]) rather than
          the default call order based ordering.

      Returns:
        A tensor representing the wrapped argument.

      Raises:
        ValueError: When indices are not consistent.
      """

# Find the appropriate index
if tag is None:
    if aggregate is not None:
        raise ValueError("You must specify `tag` if using aggregate.")
    global_index = self._get_new_global_index(index_override)
    sort_index = None
else:
    if aggregate is None:
        raise ValueError("You must specify `aggregate` if using tag.")
    if tag not in self._tag_to_global_index:
        self._tag_to_global_index[tag] = (
            self._get_new_global_index(index_override))
        self._tag_to_next_sort_index[tag] = 0
    elif (index_override and
          index_override != self._tag_to_global_index[tag]):
        raise ValueError(
            "Tag %r was called with two indices %r and %r" %
            (tag, index_override, self._tag_to_global_index[tag]))
    global_index = self._tag_to_global_index[tag]
    sort_index = self._tag_to_next_sort_index[tag]
    self._tag_to_next_sort_index[tag] += 1

uuid = self._unique_function_id
name = "%s-%s-%s-%r-%r-%s" % (self._node_name_prefix, self._function_name,
                              uuid, global_index, sort_index, name)

identity_op = _array_ops.identity(arg, name=name)

# pylint: disable=protected-access
identity_op.op._set_attr(
    OpHint.FUNCTION_NAME_ATTR,
    _attr_value_pb2.AttrValue(
        s=_compat.as_bytes(self._function_name)))
identity_op.op._set_attr(
    OpHint.FUNCTION_UUID_ATTR,
    _attr_value_pb2.AttrValue(
        s=_compat.as_bytes(self._unique_function_id)))
identity_op.op._set_attr(
    self._attr_name, _attr_value_pb2.AttrValue(i=global_index))
identity_op.op._set_attr(OpHint.FUNCTION_LEVEL_ATTR,
                         _attr_value_pb2.AttrValue(i=self._level))
if self._children_inputs_mappings:
    identity_op.op._set_attr(
        OpHint.CHILDREN_INPUTS_MAPPINGS,
        _attr_value_pb2.AttrValue(
            s=_compat.as_bytes(_json.dumps(
                self._children_inputs_mappings))))

if sort_index is not None:
    identity_op.op._set_attr(
        OpHint.FUNCTION_SORT_INDEX_ATTR,
        _attr_value_pb2.AttrValue(i=sort_index))
if aggregate is not None:
    identity_op.op._set_attr(
        OpHint.FUNCTION_AGGREGATE_ATTR,
        _attr_value_pb2.AttrValue(s=_compat.as_bytes((aggregate))))
# pylint: enable=protected-access
exit(identity_op)
