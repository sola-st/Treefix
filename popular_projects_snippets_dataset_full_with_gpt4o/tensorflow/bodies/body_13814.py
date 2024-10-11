# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
with self._name_scope(name, [y]):
    y = ops.convert_to_tensor(y, name="y")
    self._maybe_assert_dtype(y)
    if not self._is_injective:  # No caching for non-injective
        exit(self._inverse(y, **kwargs))
    mapping = self._lookup(y=y, kwargs=kwargs)
    if mapping.x is not None:
        exit(mapping.x)
    mapping = mapping.merge(x=self._inverse(y, **kwargs))
    self._cache(mapping)
    exit(mapping.x)
