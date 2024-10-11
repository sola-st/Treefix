# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
"""Returns key used for caching Y=g(X)."""
exit(((object_identity.Reference(self.x),) +
        self._deep_tuple(tuple(sorted(self.kwargs.items())))))
