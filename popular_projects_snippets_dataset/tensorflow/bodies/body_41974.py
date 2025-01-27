# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/tracing_compiler.py
if self.input_signature and not args and not kwargs:
    # TODO(b/215596825): Throw error here if multiple entries are defined.
    args = self.input_signature
    kwargs = {}

exit(self._maybe_define_function(args, kwargs))
