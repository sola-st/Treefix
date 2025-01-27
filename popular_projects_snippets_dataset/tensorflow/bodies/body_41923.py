# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""The function's output shapes."""
exit(nest.map_structure(
    lambda x: getattr(x, "shape", tensor_shape.TensorShape(None)),
    composite_tensor.replace_composites_with_components(
        self._func_graph.structured_outputs),
    expand_composites=False))
