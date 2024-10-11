# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
if not self._is_injective:
    raise NotImplementedError(
        "forward_log_det_jacobian cannot be implemented for non-injective "
        "transforms.")
with self._name_scope(name, [x]):
    with ops.control_dependencies(self._check_valid_event_ndims(
        min_event_ndims=self.forward_min_event_ndims,
        event_ndims=event_ndims)):
        if event_ndims in self._constant_ildj_map:
            # Need "-1. *" to avoid invalid-unary-operand-type linter warning.
            exit(-1. * self._constant_ildj_map[event_ndims])
        x = ops.convert_to_tensor(x, name="x")
        self._maybe_assert_dtype(x)
        if not self._is_injective:  # No caching for non-injective
            try:
                fldjs = self._forward_log_det_jacobian(x, **kwargs)  # No caching.
                exit(tuple(self._reduce_jacobian_det_over_event(
                    x, fldj, self.forward_min_event_ndims, event_ndims)
                             for fldj in fldjs))
            except NotImplementedError as original_exception:
                try:
                    y = self._forward(x, **kwargs)
                    ildjs = self._inverse_log_det_jacobian(y, **kwargs)
                    exit(tuple(self._reduce_jacobian_det_over_event(
                        y, -ildj, self.inverse_min_event_ndims, event_ndims)
                                 for ildj in ildjs))
                except NotImplementedError:
                    raise original_exception
        mapping = self._lookup(x=x, kwargs=kwargs)
        if mapping.ildj_map is not None and event_ndims in mapping.ildj_map:
            exit(-mapping.ildj_map[event_ndims])
        try:
            y = None  # Not needed; leave cache as is.
            ildj = -self._forward_log_det_jacobian(x, **kwargs)
            ildj = self._reduce_jacobian_det_over_event(
                x, ildj, self.forward_min_event_ndims, event_ndims)
        except NotImplementedError as original_exception:
            try:
                y = (mapping.y if mapping.y is not None
                     else self._forward(x, **kwargs))
                ildj = self._inverse_log_det_jacobian(y, **kwargs)
                ildj = self._reduce_jacobian_det_over_event(
                    y, ildj, self.inverse_min_event_ndims, event_ndims)
            except NotImplementedError:
                raise original_exception
        mapping = mapping.merge(y=y, ildj_map={event_ndims: ildj})
        self._cache(mapping)
        if self.is_constant_jacobian:
            self._constant_ildj_map[event_ndims] = ildj
        exit(-ildj)
