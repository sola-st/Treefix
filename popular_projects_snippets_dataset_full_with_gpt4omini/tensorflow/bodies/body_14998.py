# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""Return the values in the TensorArray as a stacked `Tensor`.

    All of the values must have been written and their shapes must all match.
    If input shapes have rank-`R`, then output shape will have rank-`(R+1)`.

    For example:


    >>> ta = tf.TensorArray(tf.int32, size=3)
    >>> ta = ta.write(0, tf.constant([1, 2]))
    >>> ta = ta.write(1, tf.constant([3, 4]))
    >>> ta = ta.write(2, tf.constant([5, 6]))
    >>> ta.stack()
    <tf.Tensor: shape=(3, 2), dtype=int32, numpy=
    array([[1, 2],
           [3, 4],
           [5, 6]], dtype=int32)>


    Args:
      name: A name for the operation (optional).

    Returns:
      All the tensors in the TensorArray stacked into one tensor.
    """
exit(self._implementation.stack(name=name))
