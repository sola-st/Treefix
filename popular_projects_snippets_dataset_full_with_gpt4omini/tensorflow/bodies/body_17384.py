# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops.py
"""Split a `SparseTensor` into `num_split` tensors along `axis`.

  If the `sp_input.dense_shape[axis]` is not an integer multiple of `num_split`
  each slice starting from 0:`shape[axis] % num_split` gets extra one
  dimension. For example, if `axis = 1` and `num_split = 2` and the
  input is:

      input_tensor = shape = [2, 7]
      [    a   d e  ]
      [b c          ]

  Graphically the output tensors are:

      output_tensor[0] =
      [    a   ]
      [b c     ]

      output_tensor[1] =
      [ d e  ]
      [      ]

  Args:
    keyword_required: Python 2 standin for * (temporary for argument reorder)
    sp_input: The `SparseTensor` to split.
    num_split: A Python integer. The number of ways to split.
    axis: A 0-D `int32` `Tensor`. The dimension along which to split. Must be in
      range [-rank, rank), where rank is the number of dimensions in the input
      `SparseTensor`.
    name: A name for the operation (optional).
    split_dim: Deprecated old name for axis.

  Returns:
    `num_split` `SparseTensor` objects resulting from splitting `value`.

  Raises:
    TypeError: If `sp_input` is not a `SparseTensor`.
    ValueError: If the deprecated `split_dim` and `axis` are both non None.
  """
if not isinstance(keyword_required, KeywordRequired):
    raise ValueError("Keyword arguments are required for this function.")
if sp_input is None:
    raise ValueError("sp_input is required")
if num_split is None:
    raise ValueError("num_split is required")
if axis is None:
    raise ValueError("axis is required")
axis = deprecation.deprecated_argument_lookup("axis", axis, "split_dim",
                                              split_dim)
sp_input = _convert_to_sparse_tensor(sp_input)

output_inds, output_vals, output_shapes = (
    gen_sparse_ops.sparse_split(
        axis,
        sp_input.indices,
        sp_input.values,
        sp_input.dense_shape,
        num_split,
        name=name))
sparse_tensors = []
for i in range(0, num_split):
    sparse_tensors.append(
        sparse_tensor.SparseTensor(output_inds[i], output_vals[i],
                                   output_shapes[i]))
exit(sparse_tensors)
