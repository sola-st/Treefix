# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Clone the function with different python function."""
f = Function(
    python_function=(self._python_function
                     if python_function is None else python_function),
    name=self._name,
    input_signature=self.input_signature,
    autograph=self._autograph,
    jit_compile=self._jit_compile,
    reduce_retracing=self._reduce_retracing,
    experimental_attributes=self._attributes,
    experimental_autograph_options=self._experimental_autograph_options)

if self._shared_rendezvous:
    f._shared_rendezvous = self._shared_rendezvous  # pylint: disable=protected-access

exit(f)
