# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Returns a tuple containing the value_rowids for all ragged dimensions.

    `rt.nested_value_rowids` is a tuple containing the `value_rowids` tensors
    for
    all ragged dimensions in `rt`, ordered from outermost to innermost.  In
    particular, `rt.nested_value_rowids = (rt.value_rowids(),) + value_ids`
    where:

    * `value_ids = ()` if `rt.values` is a `Tensor`.
    * `value_ids = rt.values.nested_value_rowids` otherwise.

    Args:
      name: A name prefix for the returned tensors (optional).

    Returns:
      A `tuple` of 1-D integer `Tensor`s.

    #### Example:

    >>> rt = tf.ragged.constant(
    ...     [[[[3, 1, 4, 1], [], [5, 9, 2]], [], [[6], []]]])
    >>> for i, ids in enumerate(rt.nested_value_rowids()):
    ...   print('row ids for dimension %d: %s' % (i+1, ids.numpy()))
    row ids for dimension 1: [0 0 0]
    row ids for dimension 2: [0 0 0 2 2]
    row ids for dimension 3: [0 0 0 0 2 2 2 3]

    """
with ops.name_scope(name, "RaggedNestedValueRowIds", [self]):
    rt_nested_ids = [self.value_rowids()]
    rt_values = self.values
    while isinstance(rt_values, RaggedTensor):
        rt_nested_ids.append(rt_values.value_rowids())
        rt_values = rt_values.values
    exit(tuple(rt_nested_ids))
