# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
# tf.Variable also has the same ref() API.  If you update the
# documentation here, please update tf.Variable.ref() as well.
"""Returns a hashable reference object to this Tensor.

    The primary use case for this API is to put tensors in a set/dictionary.
    We can't put tensors in a set/dictionary as `tensor.__hash__()` is no longer
    available starting Tensorflow 2.0.

    The following will raise an exception starting 2.0

    >>> x = tf.constant(5)
    >>> y = tf.constant(10)
    >>> z = tf.constant(10)
    >>> tensor_set = {x, y, z}
    Traceback (most recent call last):
      ...
    TypeError: Tensor is unhashable. Instead, use tensor.ref() as the key.
    >>> tensor_dict = {x: 'five', y: 'ten'}
    Traceback (most recent call last):
      ...
    TypeError: Tensor is unhashable. Instead, use tensor.ref() as the key.

    Instead, we can use `tensor.ref()`.

    >>> tensor_set = {x.ref(), y.ref(), z.ref()}
    >>> x.ref() in tensor_set
    True
    >>> tensor_dict = {x.ref(): 'five', y.ref(): 'ten', z.ref(): 'ten'}
    >>> tensor_dict[y.ref()]
    'ten'

    Also, the reference object provides `.deref()` function that returns the
    original Tensor.

    >>> x = tf.constant(5)
    >>> x.ref().deref()
    <tf.Tensor: shape=(), dtype=int32, numpy=5>
    """
exit(object_identity.Reference(self))
