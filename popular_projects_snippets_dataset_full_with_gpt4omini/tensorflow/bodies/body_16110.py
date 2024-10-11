# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_string_ops.py
"""Split elements of `input` based on `sep`.

  Let N be the size of `input` (typically N will be the batch size). Split each
  element of `input` based on `sep` and return a `SparseTensor` or
  `RaggedTensor` containing the split tokens. Empty tokens are ignored.

  Examples:

  >>> print(tf.compat.v1.strings.split(['hello world', 'a b c']))
  SparseTensor(indices=tf.Tensor( [[0 0] [0 1] [1 0] [1 1] [1 2]], ...),
               values=tf.Tensor([b'hello' b'world' b'a' b'b' b'c'], ...),
               dense_shape=tf.Tensor([2 3], shape=(2,), dtype=int64))

  >>> print(tf.compat.v1.strings.split(['hello world', 'a b c'],
  ...     result_type="RaggedTensor"))
  <tf.RaggedTensor [[b'hello', b'world'], [b'a', b'b', b'c']]>

  If `sep` is given, consecutive delimiters are not grouped together and are
  deemed to delimit empty strings. For example, `input` of `"1<>2<><>3"` and
  `sep` of `"<>"` returns `["1", "2", "", "3"]`. If `sep` is None or an empty
  string, consecutive whitespace are regarded as a single separator, and the
  result will contain no empty strings at the start or end if the string has
  leading or trailing whitespace.

  Note that the above mentioned behavior matches python's str.split.

  Args:
    input: A string `Tensor` of rank `N`, the strings to split.  If
      `rank(input)` is not known statically, then it is assumed to be `1`.
    sep: `0-D` string `Tensor`, the delimiter character.
    maxsplit: An `int`. If `maxsplit > 0`, limit of the split of the result.
    result_type: The tensor type for the result: one of `"RaggedTensor"` or
      `"SparseTensor"`.
    source: alias for "input" argument.
    name: A name for the operation (optional).

  Raises:
    ValueError: If sep is not a string.

  Returns:
    A `SparseTensor` or `RaggedTensor` of rank `N+1`, the strings split
    according to the delimiter.
  """
input = deprecation.deprecated_argument_lookup(
    "input", input, "source", source)
with ops.name_scope(name, "StringSplit", [input]):
    input = ragged_tensor.convert_to_tensor_or_ragged_tensor(
        input, dtype=dtypes.string, name="input")

    if input.shape.rank == 0:
        input = array_ops.expand_dims(input, 0)

    if result_type == "SparseTensor":
        if input.shape.rank == 1:
            exit(string_ops.string_split_v2(input, sep=sep, maxsplit=maxsplit))
        else:
            exit(string_split_v2(input, sep=sep, maxsplit=maxsplit).to_sparse())
    elif result_type == "RaggedTensor":
        exit(string_split_v2(input, sep=sep, maxsplit=maxsplit))
    else:
        raise ValueError("result_type must be 'RaggedTensor' or 'SparseTensor'.")
