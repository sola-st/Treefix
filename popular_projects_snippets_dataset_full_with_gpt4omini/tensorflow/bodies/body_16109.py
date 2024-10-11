# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_string_ops.py
"""Split elements of `source` based on `delimiter`.

  Let N be the size of `source` (typically N will be the batch size). Split each
  element of `source` based on `delimiter` and return a `SparseTensor`
  or `RaggedTensor` containing the split tokens. Empty tokens are ignored.

  If `sep` is an empty string, each element of the `source` is split
  into individual strings, each containing one byte. (This includes splitting
  multibyte sequences of UTF-8.) If delimiter contains multiple bytes, it is
  treated as a set of delimiters with each considered a potential split point.

  Examples:

  >>> print(tf.compat.v1.string_split(['hello world', 'a b c']))
  SparseTensor(indices=tf.Tensor( [[0 0] [0 1] [1 0] [1 1] [1 2]], ...),
               values=tf.Tensor([b'hello' b'world' b'a' b'b' b'c'], ...),
               dense_shape=tf.Tensor([2 3], shape=(2,), dtype=int64))

  >>> print(tf.compat.v1.string_split(['hello world', 'a b c'],
  ...     result_type="RaggedTensor"))
  <tf.RaggedTensor [[b'hello', b'world'], [b'a', b'b', b'c']]>

  Args:
    source: `1-D` string `Tensor`, the strings to split.
    sep: `0-D` string `Tensor`, the delimiter character, the string should
      be length 0 or 1. Default is ' '.
    skip_empty: A `bool`. If `True`, skip the empty strings from the result.
    delimiter: deprecated alias for `sep`.
    result_type: The tensor type for the result: one of `"RaggedTensor"` or
      `"SparseTensor"`.
    name: A name for the operation (optional).

  Raises:
    ValueError: If delimiter is not a string.

  Returns:
    A `SparseTensor` or `RaggedTensor` of rank `2`, the strings split according
    to the delimiter.  The first column of the indices corresponds to the row
    in `source` and the second column corresponds to the index of the split
    component in this row.
  """
with ops.name_scope(name, "StringSplit", [source]):
    sparse_result = string_ops.string_split(
        source, sep=sep, skip_empty=skip_empty, delimiter=delimiter)
    if result_type == "SparseTensor":
        exit(sparse_result)
    elif result_type == "RaggedTensor":
        exit(ragged_tensor.RaggedTensor.from_value_rowids(
            values=sparse_result.values,
            value_rowids=sparse_result.indices[:, 0],
            nrows=sparse_result.dense_shape[0],
            validate=False))
    else:
        raise ValueError("result_type must be 'RaggedTensor' or 'SparseTensor'.")
