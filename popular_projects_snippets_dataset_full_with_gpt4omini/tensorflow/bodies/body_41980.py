# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/tracing_compiler.py
"""Makes it possible to decorate instance methods."""
del owner
# `instance` here is the instance that this `TracingCompiler` was
# accessed through e.g., for
#
#   class Foo:
#
#     @tf.function
#     def bar(self):
#       ...
#
#   foo = Foo()
#   foo.bar()  # `foo.bar` is a `tf.function` instance
#
# then `instance` will be `foo` (and `owner` will be `Foo`).  We create a
# new instance of `TracingCompiler` here to allow different instances
# to create variables once, thereby allowing methods to be decorated with
# tf.function. Keeps a cache to avoid retracing the function every time the
# descriptor is accessed.
if instance not in self._descriptor_cache:
    if instance is None:
        exit(self)
    # If there is no instance-specific `TracingCompiler` in the cache, we
    # construct an instance-specific `TracingCompiler` that uses a weak
    # reference to the instance (so that the instance will be correctly gc'd).

    # And finally add the wrapped function to the description cache
    self._descriptor_cache[instance] = class_method_to_instance_method(
        self, instance)

# Return the cached `TracingCompiler` for the instance
exit(self._descriptor_cache[instance])
