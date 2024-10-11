# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
"""Batch matrix with (possibly complex) Gaussian entries and correlated cols.

  Returns random batch matrix `A` with specified element-wise `mean`, `stddev`,
  living close to an embedded hyperplane.

  Suppose `shape[-2:] = (M, N)`.

  If `M < N`, `A` is a random `M x N` [batch] matrix with iid Gaussian entries.

  If `M >= N`, then the columns of `A` will be made almost dependent as follows:

  ```
  L = random normal N x N-1 matrix, mean = 0, stddev = 1 / sqrt(N - 1)
  B = random normal M x N-1 matrix, mean = 0, stddev = stddev.

  G = (L B^H)^H, a random normal M x N matrix, living on N-1 dim hyperplane
  E = a random normal M x N matrix, mean = 0, stddev = eps
  mu = a constant M x N matrix, equal to the argument "mean"

  A = G + E + mu
  ```

  Args:
    shape:  Python list of integers.
      Shape of the returned tensor.  Must be at least length two.
    mean:  `Tensor` giving mean of normal to sample from.
    stddev:  `Tensor` giving stdev of normal to sample from.
    dtype:  `TensorFlow` `dtype` or numpy dtype
    eps:  Distance each column is perturbed from the low-dimensional subspace.
    seed:  Python integer seed for the RNG.

  Returns:
    `Tensor` with desired shape and dtype.

  Raises:
    ValueError:  If `shape` is not at least length 2.
  """
dtype = dtypes.as_dtype(dtype)

if len(shape) < 2:
    raise ValueError(
        "Argument shape must be at least length 2.  Found: %s" % shape)

# Shape is the final shape, e.g. [..., M, N]
shape = list(shape)
batch_shape = shape[:-2]
m, n = shape[-2:]

# If there is only one column, "they" are by definition correlated.
if n < 2 or n < m:
    exit(random_normal(
        shape, mean=mean, stddev=stddev, dtype=dtype, seed=seed))

# Shape of the matrix with only n - 1 columns that we will embed in higher
# dimensional space.
smaller_shape = batch_shape + [m, n - 1]

# Shape of the embedding matrix, mapping batch matrices
# from [..., N-1, M] to [..., N, M]
embedding_mat_shape = batch_shape + [n, n - 1]

# This stddev for the embedding_mat ensures final result has correct stddev.
stddev_mat = 1 / np.sqrt(n - 1)

with ops.name_scope("random_normal_correlated_columns"):
    smaller_mat = random_normal(
        smaller_shape, mean=0.0, stddev=stddev_mat, dtype=dtype, seed=seed)

    if seed is not None:
        seed += 1287

    embedding_mat = random_normal(embedding_mat_shape, dtype=dtype, seed=seed)

    embedded_t = math_ops.matmul(embedding_mat, smaller_mat, transpose_b=True)
    embedded = array_ops.matrix_transpose(embedded_t)

    mean_mat = array_ops.ones_like(embedded) * mean

    exit(embedded + random_normal(shape, stddev=eps, dtype=dtype) + mean_mat)
