# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Returns external Tensors captured by this function.

    self.__call__(*args) passes `args + self.captured_inputs` to the function.
    """
exit(nest.flatten(
    [x() if callable(x) else x for x in self._captured_inputs],
    expand_composites=True))
