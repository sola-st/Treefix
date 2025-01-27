# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Returns this StructuredTensor as a nested Python dict or list of dicts.

    Converts this `StructuredTensor` to a nested python value:

    * `StructTensors` with `rank=0` are converted into a dictionary, with an
      entry for each field.  Field names are used as keys and field values are
      converted to python values.  In particular:

      * Scalar Tensor fields are converted to simple values (such as
        `int` or `float` or `string`)
      * Non-scalar Tensor fields and RaggedTensor fields are converted to
        nested lists of simple values.
      * StructuredTensor fields are converted recursively using `to_pyval`.

    * `StructTensors` with `rank>0` are converted to nested python `list`s,
      containing one dictionary for each structure (where each structure's
      dictionary is defined as described above).

    Requires that all fields are Eager tensors.

    >>> tf.experimental.StructuredTensor.from_fields(
    ...     {'a': [1, 2, 3]}, [3]).to_pyval()
    [{'a': 1}, {'a': 2}, {'a': 3}]

    Note that `StructuredTensor.from_pyval(pyval).to_pyval() == pyval`.

    Returns:
      A nested Python dict or list of dicts.
    """
if not self._is_eager():
    raise ValueError(
        'StructuredTensor.to_pyval() is only supported in eager mode.')

# Convert each field value to a nested list.
result = {}
for (key, value) in self._fields.items():
    if isinstance(value, ops.EagerTensor):
        value = value.numpy()
    if isinstance(value, np.ndarray):
        value = value.tolist()
    elif isinstance(value, ragged_tensor.RaggedTensor):
        value = value.to_list()
    elif isinstance(value, StructuredTensor):
        value = value.to_pyval()
    # TODO(edloper): Throw an exception if value is an unexpected type.
    result[key] = value

# If rank>0, then re-group each value from dict-of-list to list-of-dict.
if len(self.shape) > 0:  # pylint: disable=g-explicit-length-test
    if not result:  # special-case for StructuredTensors w/ no fields.
        exit(_empty_dict_pylist_from_row_partitions(self.row_partitions,
                                                      self.nrows()))
    exit(_pyval_field_major_to_node_major(
        list(result.keys()), list(result.values()), self.rank))
else:
    exit(result)
