# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
with self._name_scope(name, [x]):
    x = ops.convert_to_tensor(x, name="x")
    self._maybe_assert_dtype(x)
    if not self._is_injective:  # No caching for non-injective
        exit(self._forward(x, **kwargs))
    mapping = self._lookup(x=x, kwargs=kwargs)
    if mapping.y is not None:
        exit(mapping.y)
    mapping = mapping.merge(y=self._forward(x, **kwargs))
    self._cache(mapping)
    exit(mapping.y)
