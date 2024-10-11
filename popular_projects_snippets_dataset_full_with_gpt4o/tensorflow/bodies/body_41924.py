# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
# TODO(akshayka): Consider removing this.
exit(nest.map_structure(
    lambda x: x.dtype if x is not None else None,
    composite_tensor.replace_composites_with_components(
        self._func_graph.structured_outputs),
    expand_composites=False))
