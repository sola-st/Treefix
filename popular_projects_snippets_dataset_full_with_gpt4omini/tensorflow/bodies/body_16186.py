# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Creates a `RaggedTensor` with rows partitioned by `uniform_row_length`.

    This method can be used to create `RaggedTensor`s with multiple uniform
    outer dimensions.  For example, a `RaggedTensor` with shape `[2, 2, None]`
    can be constructed with this method from a `RaggedTensor` values with shape
    `[4, None]`:

    >>> values = tf.ragged.constant([[1, 2, 3], [4], [5, 6], [7, 8, 9, 10]])
    >>> print(values.shape)
    (4, None)
    >>> rt1 = tf.RaggedTensor.from_uniform_row_length(values, 2)
    >>> print(rt1)
    <tf.RaggedTensor [[[1, 2, 3], [4]], [[5, 6], [7, 8, 9, 10]]]>
    >>> print(rt1.shape)
    (2, 2, None)

    Note that `rt1` only contains one ragged dimension (the innermost
    dimension). In contrast, if `from_row_splits` is used to construct a similar
    `RaggedTensor`, then that `RaggedTensor` will have two ragged dimensions:

    >>> rt2 = tf.RaggedTensor.from_row_splits(values, [0, 2, 4])
    >>> print(rt2.shape)
    (2, None, None)

    Args:
      values: A potentially ragged tensor with shape `[nvals, ...]`.
      uniform_row_length: A scalar integer tensor.  Must be nonnegative. The
        size of the outer axis of `values` must be evenly divisible by
        `uniform_row_length`.
      nrows: The number of rows in the constructed RaggedTensor.  If not
        specified, then it defaults to `nvals/uniform_row_length` (or `0` if
        `uniform_row_length==0`).  `nrows` only needs to be specified if
        `uniform_row_length` might be zero.  `uniform_row_length*nrows` must be
        `nvals`.
      validate: If true, then use assertions to check that the arguments form
        a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
          since they must be checked for each tensor value.
      name: A name prefix for the RaggedTensor (optional).

    Returns:
      A `RaggedTensor` that corresponds with the python list defined by:

      ```python
      result = [[values.pop(0) for i in range(uniform_row_length)]
                for _ in range(nrows)]
      ```

      `result.rank = values.rank + 1`.
      `result.ragged_rank = values.ragged_rank + 1`.
    """
if not isinstance(validate, bool):
    raise TypeError(f"Argument `validate` must have type bool. "
                    f"Received {validate}.")
with ops.name_scope(name, "RaggedFromUniformRowLength",
                    [values, uniform_row_length, nrows]):
    values = _convert_to_ragged_tensor_values(values)
    uniform_row_length = _convert_row_partition(
        uniform_row_length, "UniformRowLength",
        _get_optional_partition_dtype(values))
    nvals = _nvals_uniform_row_length(values, uniform_row_length)
    row_partition = RowPartition.from_uniform_row_length(
        uniform_row_length=uniform_row_length,
        nvals=nvals,
        nrows=nrows,
        validate=validate,
        dtype_hint=_get_optional_partition_dtype(values))
    exit(cls._from_row_partition(values, row_partition, validate=validate))
