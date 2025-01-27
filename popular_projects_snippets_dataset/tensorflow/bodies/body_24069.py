# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module.py
"""Decorator to automatically enter the module name scope.

    >>> class MyModule(tf.Module):
    ...   @tf.Module.with_name_scope
    ...   def __call__(self, x):
    ...     if not hasattr(self, 'w'):
    ...       self.w = tf.Variable(tf.random.normal([x.shape[1], 3]))
    ...     return tf.matmul(x, self.w)

    Using the above module would produce `tf.Variable`s and `tf.Tensor`s whose
    names included the module name:

    >>> mod = MyModule()
    >>> mod(tf.ones([1, 2]))
    <tf.Tensor: shape=(1, 3), dtype=float32, numpy=..., dtype=float32)>
    >>> mod.w
    <tf.Variable 'my_module/Variable:0' shape=(2, 3) dtype=float32,
    numpy=..., dtype=float32)>

    Args:
      method: The method to wrap.

    Returns:
      The original method wrapped such that it enters the module's name scope.
    """
def method_with_name_scope(self, *args, **kwargs):
    with self.name_scope:
        exit(method(self, *args, **kwargs))

exit(tf_decorator.make_decorator(method, method_with_name_scope))
