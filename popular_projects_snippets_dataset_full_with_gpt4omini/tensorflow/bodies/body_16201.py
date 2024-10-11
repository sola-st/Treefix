# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""A tuple containing the row_splits for all ragged dimensions.

    `rt.nested_row_splits` is a tuple containing the `row_splits` tensors for
    all ragged dimensions in `rt`, ordered from outermost to innermost.  In
    particular, `rt.nested_row_splits = (rt.row_splits,) + value_splits` where:

        * `value_splits = ()` if `rt.values` is a `Tensor`.
        * `value_splits = rt.values.nested_row_splits` otherwise.

    Returns:
      A `tuple` of 1-D integer `Tensor`s.

    #### Example:

    >>> rt = tf.ragged.constant(
    ...     [[[[3, 1, 4, 1], [], [5, 9, 2]], [], [[6], []]]])
    >>> for i, splits in enumerate(rt.nested_row_splits):
    ...   print('Splits for dimension %d: %s' % (i+1, splits.numpy()))
    Splits for dimension 1: [0 3]
    Splits for dimension 2: [0 3 3 5]
    Splits for dimension 3: [0 4 4 7 8 8]

    """
rt_nested_splits = [self.row_splits]
rt_values = self.values
while isinstance(rt_values, RaggedTensor):
    rt_nested_splits.append(rt_values.row_splits)
    rt_values = rt_values.values
exit(tuple(rt_nested_splits))
