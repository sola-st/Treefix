# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Initializes a `Function`.

    Args:
      python_function: the function to be wrapped.
      name: the name given to it.
      input_signature: See the documentation for `tf.function`.
      autograph: See the documentation for `tf.function`.
      jit_compile: See the documentation for `tf.function`.
      reduce_retracing: See the documentation for `tf.function`.
      experimental_implements: See the documentation for `tf.function`.
      experimental_autograph_options: See the documentation for `tf.function`.
      experimental_attributes: See the documentation for `tf.function`.

    Raises:
      ValueError: if `input_signature` is not None and the `python_function`'s
        argspec has keyword arguments.
    """
self._lock = threading.RLock()
self._python_function = python_function
self._function_spec = function_spec_lib.FunctionSpec.from_function_and_signature(
    python_function,
    input_signature,
    jit_compile=jit_compile,
)

self._attributes = {}
if experimental_implements is not None:
    self._attributes = self._create_implements_attribute(
        experimental_implements
    )

if experimental_attributes is not None:
    self._attributes.update(experimental_attributes)

for attribute in self._attributes:
    if attribute not in attributes_lib.POLYMORPHIC_FUNCTION_ALLOWLIST:
        raise ValueError(
            f"`{attribute} is not supported by tf.function as an attribute."
        )

    # If `True`, the function uses the rendezvous of the parent. This is only
    # needed to support code where raw send/recv operations are inserted and
    # when functions are run in graph mode where they may not be inlined.
self._shared_rendezvous = None
self._autograph = autograph
self._experimental_autograph_options = experimental_autograph_options
self._reduce_retracing = reduce_retracing
self._jit_compile = jit_compile
self._created_variables = None  # GUARDED_BY(self._lock)
self._variable_creation_fn = None  # GUARDED_BY(self._lock)
self._no_variable_creation_fn = None  # GUARDED_BY(self._lock)
self._descriptor_cache = weakref.WeakKeyDictionary()
self._name = name
self._key_for_call_stats = self._get_key_for_call_stats()
self._omit_frequent_tracing_warning = False
ops._tf_function_api_gauge.get_cell().set(True)  # pylint: disable=protected-access
