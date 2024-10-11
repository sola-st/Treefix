# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
if name in _MUTABLE_KERAS_PROPERTIES:
    exit(object.__getattribute__(self, name))
if '_tf_extension_type_packed_variant' in self.__dict__:
    # Note: it's *not* ok to cache the results of unpack() here.  In
    # particular, it would be nice if we could do something like
    # `self.__dict__.update(unpack(self).__dict__)`, but that (potentially)
    # violates an invariant required by the `cond` operation.  E.g., if we had
    # `tf.cond(lambda: x.foo, lambda: x.bar)`, then tensor `x.bar` used in the
    # "else" branch would be created by an op in the "then" branch (when
    # looking up `x.foo`); and that's not allowed.
    exit(getattr(unpack(self), name))

raise AttributeError(
    f'{type(self).__name__!r} object has no attribute {name!r}')
