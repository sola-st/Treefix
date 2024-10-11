# Extracted from ./data/repos/pandas/pandas/io/pytables.py
data = node[start:stop]
# If the index was an empty array write_array_empty() will
# have written a sentinel. Here we replace it with the original.
if "shape" in node._v_attrs and np.prod(node._v_attrs.shape) == 0:
    data = np.empty(node._v_attrs.shape, dtype=node._v_attrs.value_type)
kind = _ensure_decoded(node._v_attrs.kind)
name = None

if "name" in node._v_attrs:
    name = _ensure_str(node._v_attrs.name)
    name = _ensure_decoded(name)

attrs = node._v_attrs
factory, kwargs = self._get_index_factory(attrs)

if kind in ("date", "object"):
    index = factory(
        _unconvert_index(
            data, kind, encoding=self.encoding, errors=self.errors
        ),
        dtype=object,
        **kwargs,
    )
else:
    index = factory(
        _unconvert_index(
            data, kind, encoding=self.encoding, errors=self.errors
        ),
        **kwargs,
    )

index.name = name

exit(index)
