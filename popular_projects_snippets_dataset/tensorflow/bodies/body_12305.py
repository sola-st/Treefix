# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
r"""Gather slices from params axis `axis` according to indices.

  Gather slices from `params` axis `axis` according to `indices`.  `indices`
  must be an integer tensor of any dimension (often 1-D).

  `Tensor.__getitem__` works for scalars, `tf.newaxis`, and
  [python slices](https://numpy.org/doc/stable/reference/arrays.indexing.html#basic-slicing-and-indexing)

  `tf.gather` extends indexing to handle tensors of indices.

  In the simplest case it's identical to scalar indexing:

  >>> params = tf.constant(['p0', 'p1', 'p2', 'p3', 'p4', 'p5'])
  >>> params[3].numpy()
  b'p3'
  >>> tf.gather(params, 3).numpy()
  b'p3'

  The most common case is to pass a single axis tensor of indices (this
  can't be expressed as a python slice because the indices are not sequential):

  >>> indices = [2, 0, 2, 5]
  >>> tf.gather(params, indices).numpy()
  array([b'p2', b'p0', b'p2', b'p5'], dtype=object)

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src="https://www.tensorflow.org/images/Gather.png"
  alt>
  </div>

  The indices can have any shape. When the `params` has 1 axis, the
  output shape is equal to the input shape:

  >>> tf.gather(params, [[2, 0], [2, 5]]).numpy()
  array([[b'p2', b'p0'],
         [b'p2', b'p5']], dtype=object)

  The `params` may also have any shape. `gather` can select slices
  across any axis depending on the `axis` argument (which defaults to 0).
  Below it is used to gather first rows, then columns from a matrix:

  >>> params = tf.constant([[0, 1.0, 2.0],
  ...                       [10.0, 11.0, 12.0],
  ...                       [20.0, 21.0, 22.0],
  ...                       [30.0, 31.0, 32.0]])
  >>> tf.gather(params, indices=[3,1]).numpy()
  array([[30., 31., 32.],
         [10., 11., 12.]], dtype=float32)
  >>> tf.gather(params, indices=[2,1], axis=1).numpy()
  array([[ 2.,  1.],
         [12., 11.],
         [22., 21.],
         [32., 31.]], dtype=float32)

  More generally: The output shape has the same shape as the input, with the
  indexed-axis replaced by the shape of the indices.

  >>> def result_shape(p_shape, i_shape, axis=0):
  ...   return p_shape[:axis] + i_shape + p_shape[axis+1:]
  >>>
  >>> result_shape([1, 2, 3], [], axis=1)
  [1, 3]
  >>> result_shape([1, 2, 3], [7], axis=1)
  [1, 7, 3]
  >>> result_shape([1, 2, 3], [7, 5], axis=1)
  [1, 7, 5, 3]

  Here are some examples:

  >>> params.shape.as_list()
  [4, 3]
  >>> indices = tf.constant([[0, 2]])
  >>> tf.gather(params, indices=indices, axis=0).shape.as_list()
  [1, 2, 3]
  >>> tf.gather(params, indices=indices, axis=1).shape.as_list()
  [4, 1, 2]

  >>> params = tf.random.normal(shape=(5, 6, 7, 8))
  >>> indices = tf.random.uniform(shape=(10, 11), maxval=7, dtype=tf.int32)
  >>> result = tf.gather(params, indices, axis=2)
  >>> result.shape.as_list()
  [5, 6, 10, 11, 8]

  This is because each index takes a slice from `params`, and
  places it at the corresponding location in the output. For the above example

  >>> # For any location in indices
  >>> a, b = 0, 1
  >>> tf.reduce_all(
  ...     # the corresponding slice of the result
  ...     result[:, :, a, b, :] ==
  ...     # is equal to the slice of `params` along `axis` at the index.
  ...     params[:, :, indices[a, b], :]
  ... ).numpy()
  True

  ### Batching:

  The `batch_dims` argument lets you gather different items from each element
  of a batch.

  Using `batch_dims=1` is equivalent to having an outer loop over the first
  axis of `params` and `indices`:

  >>> params = tf.constant([
  ...     [0, 0, 1, 0, 2],
  ...     [3, 0, 0, 0, 4],
  ...     [0, 5, 0, 6, 0]])
  >>> indices = tf.constant([
  ...     [2, 4],
  ...     [0, 4],
  ...     [1, 3]])

  >>> tf.gather(params, indices, axis=1, batch_dims=1).numpy()
  array([[1, 2],
         [3, 4],
         [5, 6]], dtype=int32)

  This is equivalent to:

  >>> def manually_batched_gather(params, indices, axis):
  ...   batch_dims=1
  ...   result = []
  ...   for p,i in zip(params, indices):
  ...     r = tf.gather(p, i, axis=axis-batch_dims)
  ...     result.append(r)
  ...   return tf.stack(result)
  >>> manually_batched_gather(params, indices, axis=1).numpy()
  array([[1, 2],
         [3, 4],
         [5, 6]], dtype=int32)

  Higher values of `batch_dims` are equivalent to multiple nested loops over
  the outer axes of `params` and `indices`. So the overall shape function is

  >>> def batched_result_shape(p_shape, i_shape, axis=0, batch_dims=0):
  ...   return p_shape[:axis] + i_shape[batch_dims:] + p_shape[axis+1:]
  >>>
  >>> batched_result_shape(
  ...     p_shape=params.shape.as_list(),
  ...     i_shape=indices.shape.as_list(),
  ...     axis=1,
  ...     batch_dims=1)
  [3, 2]

  >>> tf.gather(params, indices, axis=1, batch_dims=1).shape.as_list()
  [3, 2]

  This comes up naturally if you need to use the indices of an operation like
  `tf.argsort`, or `tf.math.top_k` where the last dimension of the indices
  indexes into the last dimension of input, at the corresponding location.
  In this case you can use `tf.gather(values, indices, batch_dims=-1)`.

  See also:

  * `tf.Tensor.__getitem__`: The direct tensor index operation (`t[]`), handles
    scalars and python-slices `tensor[..., 7, 1:-1]`
  * `tf.scatter`: A collection of operations similar to `__setitem__`
    (`t[i] = x`)
  * `tf.gather_nd`: An operation similar to `tf.gather` but gathers across
    multiple axis at once (it can gather elements of a matrix instead of rows
    or columns)
  * `tf.boolean_mask`, `tf.where`: Binary indexing.
  * `tf.slice` and `tf.strided_slice`: For lower level access to the
    implementation of `__getitem__`'s python-slice handling (`t[1:-1:2]`)

  Args:
    params: The `Tensor` from which to gather values. Must be at least rank
      `axis + 1`.
    indices: The index `Tensor`.  Must be one of the following types: `int32`,
      `int64`. The values must be in range `[0, params.shape[axis])`.
    validate_indices: Deprecated, does nothing. Indices are always validated on
      CPU, never validated on GPU.

      Caution: On CPU, if an out of bound index is found, an error is raised.
      On GPU, if an out of bound index is found, a 0 is stored in the
      corresponding output value.
    axis: A `Tensor`. Must be one of the following types: `int32`, `int64`. The
      `axis` in `params` to gather `indices` from. Must be greater than or equal
      to `batch_dims`.  Defaults to the first non-batch dimension. Supports
      negative indexes.
    batch_dims: An `integer`.  The number of batch dimensions.  Must be less
      than or equal to `rank(indices)`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `params`.
  """
del validate_indices

if axis is None:
    axis = batch_dims
if tensor_util.constant_value(axis) != 0:
    exit(gen_array_ops.gather_v2(
        params, indices, axis, batch_dims=batch_dims, name=name))
try:
    # TODO(apassos) find a less bad way of detecting resource variables
    # without introducing a circular dependency.
    exit(params.sparse_read(indices, name=name))
except AttributeError:
    exit(gen_array_ops.gather_v2(params, indices, axis, name=name))
