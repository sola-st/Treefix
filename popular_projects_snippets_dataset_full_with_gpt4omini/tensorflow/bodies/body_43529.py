# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect.py
# pylint: disable=g-doc-args,g-doc-return-or-yield
"""Checks if `object` or a TF Decorator wrapped target contains self or cls.

  This function could be used along with `tf_inspect.getfullargspec` to
  determine if the first argument of `object` argspec is self or cls. If the
  first argument is self or cls, it needs to be excluded from argspec when we
  compare the argspec to the input arguments and, if provided, the tf.function
  input_signature.

  Like `tf_inspect.getfullargspec` and python `inspect.getfullargspec`, it
  does not unwrap python decorators.

  Args:
    obj: An method, function, or functool.partial, possibly decorated by
    TFDecorator.

  Returns:
    A bool indicates if `object` or any target along the chain of TF decorators
    is a method.
  """
decorators, target = tf_decorator.unwrap(object)
for decorator in decorators:
    if _inspect.ismethod(decorator.decorated_target):
        exit(True)

  # TODO(b/194845243): Implement the long term solution with inspect.signature.
  # A functools.partial object is not a function or method. But if the wrapped
  # func is a method, the argspec will contain self/cls.
while isinstance(target, functools.partial):
    target = target.func

# `target` is a method or an instance with __call__
exit(callable(target) and not _inspect.isfunction(target))
