# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
# tf.Tensor also has the same ref() API.  If you update the
# documentation here, please update tf.Tensor.ref() as well.
"""Returns a hashable reference object to this Variable.

    The primary use case for this API is to put variables in a set/dictionary.
    We can't put variables in a set/dictionary as `variable.__hash__()` is no
    longer available starting Tensorflow 2.0.

    The following will raise an exception starting 2.0

    >>> x = tf.Variable(5)
    >>> y = tf.Variable(10)
    >>> z = tf.Variable(10)
    >>> variable_set = {x, y, z}
    Traceback (most recent call last):
      ...
    TypeError: Variable is unhashable. Instead, use tensor.ref() as the key.
    >>> variable_dict = {x: 'five', y: 'ten'}
    Traceback (most recent call last):
      ...
    TypeError: Variable is unhashable. Instead, use tensor.ref() as the key.

    Instead, we can use `variable.ref()`.

    >>> variable_set = {x.ref(), y.ref(), z.ref()}
    >>> x.ref() in variable_set
    True
    >>> variable_dict = {x.ref(): 'five', y.ref(): 'ten', z.ref(): 'ten'}
    >>> variable_dict[y.ref()]
    'ten'

    Also, the reference object provides `.deref()` function that returns the
    original Variable.

    >>> x = tf.Variable(5)
    >>> x.ref().deref()
    <tf.Variable 'Variable:0' shape=() dtype=int32, numpy=5>
    """
exit(object_identity.Reference(self))
