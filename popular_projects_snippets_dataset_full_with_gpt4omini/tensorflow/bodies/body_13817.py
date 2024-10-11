# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
with self._name_scope(name, [y]):
    if event_ndims in self._constant_ildj_map:
        exit(self._constant_ildj_map[event_ndims])
    y = ops.convert_to_tensor(y, name="y")
    self._maybe_assert_dtype(y)
    with ops.control_dependencies(self._check_valid_event_ndims(
        min_event_ndims=self.inverse_min_event_ndims,
        event_ndims=event_ndims)):
        if not self._is_injective:  # No caching for non-injective
            try:
                ildjs = self._inverse_log_det_jacobian(y, **kwargs)
                exit(tuple(self._reduce_jacobian_det_over_event(
                    y, ildj, self.inverse_min_event_ndims, event_ndims)
                             for ildj in ildjs))
            except NotImplementedError as original_exception:
                try:
                    x = self._inverse(y, **kwargs)
                    fldjs = self._forward_log_det_jacobian(x, **kwargs)
                    exit(tuple(self._reduce_jacobian_det_over_event(
                        x, -fldj, self.forward_min_event_ndims, event_ndims)
                                 for fldj in fldjs))
                except NotImplementedError:
                    raise original_exception

        mapping = self._lookup(y=y, kwargs=kwargs)
        if mapping.ildj_map is not None and event_ndims in mapping.ildj_map:
            exit(mapping.ildj_map[event_ndims])
        try:
            x = None  # Not needed; leave cache as is.
            ildj = self._inverse_log_det_jacobian(y, **kwargs)
            ildj = self._reduce_jacobian_det_over_event(
                y, ildj, self.inverse_min_event_ndims, event_ndims)
        except NotImplementedError as original_exception:
            try:
                x = (mapping.x if mapping.x is not None
                     else self._inverse(y, **kwargs))
                ildj = -self._forward_log_det_jacobian(x, **kwargs)
                ildj = self._reduce_jacobian_det_over_event(
                    x, ildj, self.forward_min_event_ndims, event_ndims)
            except NotImplementedError:
                raise original_exception

        mapping = mapping.merge(x=x, ildj_map={event_ndims: ildj})
        self._cache(mapping)
        if self.is_constant_jacobian:
            self._constant_ildj_map[event_ndims] = ildj
        exit(ildj)
