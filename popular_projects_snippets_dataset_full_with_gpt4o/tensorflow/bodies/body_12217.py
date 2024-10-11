# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Computes the difference between two lists of numbers or strings.

  Given a list x and a list y, this operation returns a list out that
  represents all values that are in x but not in y. The returned list
  out is sorted in the same order that the numbers appear in x
  (duplicates are preserved). This operation also returns a list idx
  that represents the position of each out element in x.

  In other words:

  ```python
  out[i] = x[idx[i]] for i in [0, 1, ..., len(out) - 1]
  ```

  Example usage:

  >>> x = [1, 2, 3, 4, 5, 6]
  >>> y = [1, 3, 5]
  >>> setdiff1d(x,y)
  ListDiff(out=<tf.Tensor: id=2, shape=(3,), dtype=int32,
  numpy=array([2, 4, 6], dtype=int32)>, idx=<tf.Tensor: id=3,
  shape=(3,), dtype=int32, numpy=array([1, 3, 5], dtype=int32)>)

  Args:
    x: A Tensor. 1-D. Values to keep.
    y: A Tensor. Must have the same type as x. 1-D. Values to remove.
    out_idx: An optional tf.DType from: tf.int32, tf.int64. Defaults to
      tf.int32.
    name: A name for the operation (optional).

  Returns:
    A tuple of Tensor objects (out, idx).
    out: A Tensor. Has the same type as x.
    idx: A Tensor of type out_idx.
  """
exit(gen_array_ops.list_diff(x, y, index_dtype, name))
