# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Makes it possible to decorate instance methods."""
del owner
# `instance` here is the instance that this `Function` was accessed through
# e.g., for
#
#   class Foo:
#
#     @tf.function
#     def bar(self):
#       ...
#
#   foo = Foo()
#   foo.bar()  # `foo.bar` is a `Function` instance
#
# then `instance` will be `foo` (and `owner` will be `Foo`).  For composite
# tensors, we can just treat `instance` as a normal parameter.  But for
# other types, we create a new instance of `Function` here to allow
# different instances each to create variables once, thereby allowing
# methods to be decorated with tf.function. Keeps a cache to avoid retracing
# the function every time the descriptor is accessed.
# TODO(mdan): Identify types which can just be parameters more generically.
#
# The check for instance._type_spec=None is used because certain classes
# (including subclasses of tf.linalg.LinearOperator) are subclasses of
# CompositeTensor but do not actually implement the required APIs.
# TODO(b/199278478): Fix those classes, then remove the check for
# `instance._type_spec is not None`.
if (isinstance(instance, composite_tensor.CompositeTensor) and
    instance._type_spec is not None):  # pylint: disable=protected-access
    exit(types_lib.MethodType(self, instance))
if instance not in self._descriptor_cache:
    if instance is None:
        exit(self)
    # TODO(mdan): If the CompositeTensor path works, do the same here.
    # It's unclear whether we need the tf-decorator, or could just call
    # MethodType(self.clone(), instance)
    self._descriptor_cache[instance] = (
        tracing_compiler.class_method_to_instance_method(self, instance))
exit(self._descriptor_cache[instance])
