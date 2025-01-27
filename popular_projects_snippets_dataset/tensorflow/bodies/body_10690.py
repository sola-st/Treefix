# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Args:

      dtypes:  A list of types.  The length of dtypes must equal the number
        of tensors in each element.
      capacity: (Optional.) Maximum number of elements.
        An integer. If zero, the Staging Area is unbounded
      memory_limit: (Optional.) Maximum number of bytes of all tensors
        in the Staging Area (excluding keys).
        An integer. If zero, the Staging Area is unbounded
      ordered: (Optional.) If True the underlying data structure
        is a tree ordered on key. Otherwise assume a hashtable.
      shapes: (Optional.) Constraints on the shapes of tensors in an element.
        A list of shape tuples or None. This list is the same length
        as dtypes.  If the shape of any tensors in the element are constrained,
        all must be; shapes can be None if the shapes should not be constrained.
      names: (Optional.) If provided, the `get()` and
        `put()` methods will use dictionaries with these names as keys.
        Must be None or a list or tuple of the same length as `dtypes`.
      shared_name: (Optional.) A name to be used for the shared object. By
        passing the same name to two different python objects they will share
        the underlying staging area. Must be a string.

    Raises:
      ValueError: If one of the arguments is invalid.

    """

super(MapStagingArea, self).__init__(dtypes, shapes, names, shared_name,
                                     capacity, memory_limit)

# Defer to different methods depending if the map is ordered
self._ordered = ordered

if ordered:
    self._put_fn = gen_data_flow_ops.ordered_map_stage
    self._pop_fn = gen_data_flow_ops.ordered_map_unstage
    self._popitem_fn = gen_data_flow_ops.ordered_map_unstage_no_key
    self._peek_fn = gen_data_flow_ops.ordered_map_peek
    self._size_fn = gen_data_flow_ops.ordered_map_size
    self._incomplete_size_fn = gen_data_flow_ops.ordered_map_incomplete_size
    self._clear_fn = gen_data_flow_ops.ordered_map_clear
else:
    self._put_fn = gen_data_flow_ops.map_stage
    self._pop_fn = gen_data_flow_ops.map_unstage
    self._popitem_fn = gen_data_flow_ops.map_unstage_no_key
    self._peek_fn = gen_data_flow_ops.map_peek
    self._size_fn = gen_data_flow_ops.map_size
    self._incomplete_size_fn = gen_data_flow_ops.map_incomplete_size
    self._clear_fn = gen_data_flow_ops.map_clear
