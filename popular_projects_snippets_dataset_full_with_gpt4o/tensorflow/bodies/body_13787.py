# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
"""Returns key used for caching X=g^{-1}(Y)."""
exit(((object_identity.Reference(self.y),) +
        self._deep_tuple(tuple(sorted(self.kwargs.items())))))
