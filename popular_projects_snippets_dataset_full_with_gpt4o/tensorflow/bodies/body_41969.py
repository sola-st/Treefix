# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/tracing_compiler.py
"""Initializes a `TracingCompiler`.

    Args:
      python_function: the function to be wrapped.
      name: the name given to it.
      input_signature: a possibly nested sequence of `TensorSpec` objects
        specifying the input signature of this function. If `None`, a separate
        function is instantiated for each inferred input signature.
      attributes: dict, extra keyword arguments that will be added as attribute
        of the function.
      autograph: whether to use autograph to compile `python_function`. See
        https://www.tensorflow.org/guide/autograph for more information.
      autograph_options: Experimental knobs to control behavior `when
        autograph=True`. See https://www.tensorflow.org/guide/autograph for more
        information.
      reduce_retracing: When True, `tf.function` uses
        `tf.types.experimental.TraceType` to trace supertypes of arguments to
        reduce the number of traces.
      capture_by_value: Experimental. Whether to capture resource variables by
        value or reference. If None, will inherit from a parent context or
        default to False.
      jit_compile: Force-compile the function with XLA, cf. tf.function doc on
        jit_compile.

    Raises:
      ValueError: if `input_signature` is not None and the `python_function`'s
        argspec has keyword arguments.
    """
self._python_function = python_function
pure_function = attributes and attributes_lib.IMPLEMENTS in attributes
self._function_spec = function_spec.FunctionSpec.from_function_and_signature(
    python_function, input_signature, is_pure=pure_function)
self._name = name
self._autograph = autograph
self._autograph_options = autograph_options
self._reduce_retracing = reduce_retracing
self._function_cache = function_cache.FunctionCache()

self._function_attributes = attributes or {}
for attribute in self._function_attributes:
    if attribute not in attributes_lib.TRACING_COMPILER_ALLOWLIST:
        raise ValueError(
            f"TracingCompiler does not support `{attribute}` as an attribute."
        )

self._capture_by_value = capture_by_value
self.tracing_count = 0
# Maintein a dict of all captures: identifier -> lambda function. It's used
# to get runtime values for all captures during ConcreteFunction dispatch,
self._func_captures = capture_container.FunctionCaptures()
self._lock = threading.RLock()
# _descriptor_cache is a of instance of a class to an instance-specific
# `TracingCompiler`, used to make sure tf.function-decorated methods
# create different functions for each instance.
self._descriptor_cache = weakref.WeakKeyDictionary()
self._jit_compile = jit_compile
