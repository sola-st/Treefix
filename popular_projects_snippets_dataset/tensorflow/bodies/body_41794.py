# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Returns a TracingCompiler generated from the input function."""
attributes = self._attributes.copy()

share = self._shared_rendezvous
if share is not None:
    attributes[attributes_lib.SHARED_RENDEZVOUS] = share

if self._jit_compile is not None:
    attributes[attributes_lib.XLA_COMPILE] = bool(self._jit_compile)
    if self._jit_compile:
        attributes[attributes_lib.NO_INLINE] = True

try:
    name = fn.__name__
except AttributeError:
    name = "function"

exit(tracing_compiler.TracingCompiler(
    fn,
    name,
    input_signature=self.input_signature,
    attributes=attributes,
    autograph=self._autograph,
    jit_compile=self._jit_compile,
    reduce_retracing=self._reduce_retracing,
    autograph_options=self._experimental_autograph_options))
