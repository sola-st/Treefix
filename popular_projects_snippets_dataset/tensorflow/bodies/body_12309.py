# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
r"""Gather slices from `params` into a Tensor with shape specified by `indices`.

  `indices` is a `Tensor` of indices into `params`. The index vectors are
  arranged along the last axis of `indices`.

  This is similar to `tf.gather`, in which `indices` defines slices into the
  first dimension of `params`. In `tf.gather_nd`, `indices` defines slices into
  the first `N` dimensions of `params`, where `N = indices.shape[-1]`.

  Caution: On CPU, if an out of bound index is found, an error is returned.
  On GPU, if an out of bound index is found, a 0 is stored in the
  corresponding output value.

  ## Gathering scalars

  In the simplest case the vectors in `indices` index the full rank of `params`:

  >>> tf.gather_nd(
  ...     indices=[[0, 0],
  ...              [1, 1]],
  ...     params = [['a', 'b'],
  ...               ['c', 'd']]).numpy()
  array([b'a', b'd'], dtype=object)

  In this case the result has 1-axis fewer than `indices`, and each index vector
  is replaced by the scalar indexed from `params`.

  In this case the shape relationship is:

  ```
  index_depth = indices.shape[-1]
  assert index_depth == params.shape.rank
  result_shape = indices.shape[:-1]
  ```

  If `indices` has a rank of `K`, it is helpful to think `indices` as a
  (K-1)-dimensional tensor of indices into `params`.

  ## Gathering slices

  If the index vectors do not index the full rank of `params` then each location
  in the result contains a slice of params. This example collects rows from a
  matrix:

  >>> tf.gather_nd(
  ...     indices = [[1],
  ...                [0]],
  ...     params = [['a', 'b', 'c'],
  ...               ['d', 'e', 'f']]).numpy()
  array([[b'd', b'e', b'f'],
         [b'a', b'b', b'c']], dtype=object)

  Here `indices` contains `[2]` index vectors, each with a length of `1`.
  The index vectors each refer to rows of the `params` matrix. Each
  row has a shape of `[3]` so the output shape is `[2, 3]`.

  In this case, the relationship between the shapes is:

  ```
  index_depth = indices.shape[-1]
  outer_shape = indices.shape[:-1]
  assert index_depth <= params.shape.rank
  inner_shape = params.shape[index_depth:]
  output_shape = outer_shape + inner_shape
  ```

  It is helpful to think of the results in this case as tensors-of-tensors.
  The shape of the outer tensor is set by the leading dimensions of `indices`.
  While the shape of the inner tensors is the shape of a single slice.

  ## Batches

  Additionally, both `params` and `indices` can have `M` leading batch
  dimensions that exactly match. In this case `batch_dims` must be set to `M`.

  For example, to collect one row from each of a batch of matrices you could
  set the leading elements of the index vectors to be their location in the
  batch:

  >>> tf.gather_nd(
  ...     indices = [[0, 1],
  ...                [1, 0],
  ...                [2, 4],
  ...                [3, 2],
  ...                [4, 1]],
  ...     params=tf.zeros([5, 7, 3])).shape.as_list()
  [5, 3]

  The `batch_dims` argument lets you omit those leading location dimensions
  from the index:

  >>> tf.gather_nd(
  ...     batch_dims=1,
  ...     indices = [[1],
  ...                [0],
  ...                [4],
  ...                [2],
  ...                [1]],
  ...     params=tf.zeros([5, 7, 3])).shape.as_list()
  [5, 3]

  This is equivalent to caling a separate `gather_nd` for each location in the
  batch dimensions.


  >>> params=tf.zeros([5, 7, 3])
  >>> indices=tf.zeros([5, 1])
  >>> batch_dims = 1
  >>>
  >>> index_depth = indices.shape[-1]
  >>> batch_shape = indices.shape[:batch_dims]
  >>> assert params.shape[:batch_dims] == batch_shape
  >>> outer_shape = indices.shape[batch_dims:-1]
  >>> assert index_depth <= params.shape.rank
  >>> inner_shape = params.shape[batch_dims + index_depth:]
  >>> output_shape = batch_shape + outer_shape + inner_shape
  >>> output_shape.as_list()
  [5, 3]

  ### More examples

  Indexing into a 3-tensor:

  >>> tf.gather_nd(
  ...     indices = [[1]],
  ...     params = [[['a0', 'b0'], ['c0', 'd0']],
  ...               [['a1', 'b1'], ['c1', 'd1']]]).numpy()
  array([[[b'a1', b'b1'],
          [b'c1', b'd1']]], dtype=object)



  >>> tf.gather_nd(
  ...     indices = [[0, 1], [1, 0]],
  ...     params = [[['a0', 'b0'], ['c0', 'd0']],
  ...               [['a1', 'b1'], ['c1', 'd1']]]).numpy()
  array([[b'c0', b'd0'],
         [b'a1', b'b1']], dtype=object)


  >>> tf.gather_nd(
  ...     indices = [[0, 0, 1], [1, 0, 1]],
  ...     params = [[['a0', 'b0'], ['c0', 'd0']],
  ...               [['a1', 'b1'], ['c1', 'd1']]]).numpy()
  array([b'b0', b'b1'], dtype=object)

  The examples below are for the case when only indices have leading extra
  dimensions. If both 'params' and 'indices' have leading batch dimensions, use
  the 'batch_dims' parameter to run gather_nd in batch mode.

  Batched indexing into a matrix:

  >>> tf.gather_nd(
  ...     indices = [[[0, 0]], [[0, 1]]],
  ...     params = [['a', 'b'], ['c', 'd']]).numpy()
  array([[b'a'],
         [b'b']], dtype=object)



  Batched slice indexing into a matrix:

  >>> tf.gather_nd(
  ...     indices = [[[1]], [[0]]],
  ...     params = [['a', 'b'], ['c', 'd']]).numpy()
  array([[[b'c', b'd']],
         [[b'a', b'b']]], dtype=object)


  Batched indexing into a 3-tensor:

  >>> tf.gather_nd(
  ...     indices = [[[1]], [[0]]],
  ...     params = [[['a0', 'b0'], ['c0', 'd0']],
  ...               [['a1', 'b1'], ['c1', 'd1']]]).numpy()
  array([[[[b'a1', b'b1'],
           [b'c1', b'd1']]],
         [[[b'a0', b'b0'],
           [b'c0', b'd0']]]], dtype=object)


  >>> tf.gather_nd(
  ...     indices = [[[0, 1], [1, 0]], [[0, 0], [1, 1]]],
  ...     params = [[['a0', 'b0'], ['c0', 'd0']],
  ...               [['a1', 'b1'], ['c1', 'd1']]]).numpy()
  array([[[b'c0', b'd0'],
          [b'a1', b'b1']],
         [[b'a0', b'b0'],
          [b'c1', b'd1']]], dtype=object)

  >>> tf.gather_nd(
  ...     indices = [[[0, 0, 1], [1, 0, 1]], [[0, 1, 1], [1, 1, 0]]],
  ...     params = [[['a0', 'b0'], ['c0', 'd0']],
  ...               [['a1', 'b1'], ['c1', 'd1']]]).numpy()
  array([[b'b0', b'b1'],
         [b'd0', b'c1']], dtype=object)


  Examples with batched 'params' and 'indices':

  >>> tf.gather_nd(
  ...     batch_dims = 1,
  ...     indices = [[1],
  ...                [0]],
  ...     params = [[['a0', 'b0'],
  ...                ['c0', 'd0']],
  ...               [['a1', 'b1'],
  ...                ['c1', 'd1']]]).numpy()
  array([[b'c0', b'd0'],
         [b'a1', b'b1']], dtype=object)


  >>> tf.gather_nd(
  ...     batch_dims = 1,
  ...     indices = [[[1]], [[0]]],
  ...     params = [[['a0', 'b0'], ['c0', 'd0']],
  ...               [['a1', 'b1'], ['c1', 'd1']]]).numpy()
  array([[[b'c0', b'd0']],
         [[b'a1', b'b1']]], dtype=object)

  >>> tf.gather_nd(
  ...     batch_dims = 1,
  ...     indices = [[[1, 0]], [[0, 1]]],
  ...     params = [[['a0', 'b0'], ['c0', 'd0']],
  ...               [['a1', 'b1'], ['c1', 'd1']]]).numpy()
  array([[b'c0'],
         [b'b1']], dtype=object)


  See also `tf.gather`.

  Args:
    params: A `Tensor`. The tensor from which to gather values.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      Index tensor.
    name: A name for the operation (optional).
    batch_dims: An integer or a scalar 'Tensor'. The number of batch dimensions.

  Returns:
    A `Tensor`. Has the same type as `params`.
  """
batch_dims_ = tensor_util.constant_value(batch_dims)
if batch_dims_ is not None:
    batch_dims = int(batch_dims_)
if batch_dims == 0:
    try:
        # TODO(apassos) find a less bad way of detecting resource variables
        # without introducing a circular dependency.
        exit(params.gather_nd(indices, name=name))
    except AttributeError:
        exit(gen_array_ops.gather_nd(params, indices, name=name))
else:
    exit(batch_gather_nd(params, indices, batch_dims=batch_dims, name=name))
