# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_deserialization.py
# TODO(b/205016819): We may enable autograph once exceptions are supported.
super(RestoredFunction, self).__init__(
    python_function,
    name,
    autograph=False,
    jit_compile=function_spec.jit_compile)
self.concrete_functions = concrete_functions
self._function_spec = function_spec

# Prevent RestoredFunction from spamming users with frequent tracing
# warnings.
self._omit_frequent_tracing_warning = True
