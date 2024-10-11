# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter.py
"""Constructor.

    Args:
      model_path: Path to TF-Lite Flatbuffer file.
      model_content: Content of model.
      experimental_delegates: Experimental. Subject to change. List of
        [TfLiteDelegate](https://www.tensorflow.org/lite/performance/delegates)
          objects returned by lite.load_delegate().
      num_threads: Sets the number of threads used by the interpreter and
        available to CPU kernels. If not set, the interpreter will use an
        implementation-dependent default number of threads. Currently, only a
        subset of kernels, such as conv, support multi-threading. num_threads
        should be >= -1. Setting num_threads to 0 has the effect to disable
        multithreading, which is equivalent to setting num_threads to 1. If set
        to the value -1, the number of threads used will be
        implementation-defined and platform-dependent.
      experimental_op_resolver_type: The op resolver used by the interpreter. It
        must be an instance of OpResolverType. By default, we use the built-in
        op resolver which corresponds to tflite::ops::builtin::BuiltinOpResolver
        in C++.
      experimental_preserve_all_tensors: If true, then intermediate tensors used
        during computation are preserved for inspection, and if the passed op
        resolver type is AUTO or BUILTIN, the type will be changed to
        BUILTIN_WITHOUT_DEFAULT_DELEGATES so that no Tensorflow Lite default
        delegates are applied. If false, getting intermediate tensors could
        result in undefined values or None, especially when the graph is
        successfully modified by the Tensorflow Lite default delegate.

    Raises:
      ValueError: If the interpreter was unable to create.
    """
if not hasattr(self, '_custom_op_registerers'):
    self._custom_op_registerers = []

actual_resolver_type = experimental_op_resolver_type
if experimental_preserve_all_tensors and (
    experimental_op_resolver_type == OpResolverType.AUTO or
    experimental_op_resolver_type == OpResolverType.BUILTIN):
    actual_resolver_type = OpResolverType.BUILTIN_WITHOUT_DEFAULT_DELEGATES
op_resolver_id = _get_op_resolver_id(actual_resolver_type)
if op_resolver_id is None:
    raise ValueError('Unrecognized passed in op resolver type: {}'.format(
        experimental_op_resolver_type))

if model_path and not model_content:
    custom_op_registerers_by_name = [
        x for x in self._custom_op_registerers if isinstance(x, str)
    ]
    custom_op_registerers_by_func = [
        x for x in self._custom_op_registerers if not isinstance(x, str)
    ]
    self._interpreter = (
        _interpreter_wrapper.CreateWrapperFromFile(
            model_path, op_resolver_id, custom_op_registerers_by_name,
            custom_op_registerers_by_func, experimental_preserve_all_tensors))
    if not self._interpreter:
        raise ValueError('Failed to open {}'.format(model_path))
elif model_content and not model_path:
    custom_op_registerers_by_name = [
        x for x in self._custom_op_registerers if isinstance(x, str)
    ]
    custom_op_registerers_by_func = [
        x for x in self._custom_op_registerers if not isinstance(x, str)
    ]
    # Take a reference, so the pointer remains valid.
    # Since python strings are immutable then PyString_XX functions
    # will always return the same pointer.
    self._model_content = model_content
    self._interpreter = (
        _interpreter_wrapper.CreateWrapperFromBuffer(
            model_content, op_resolver_id, custom_op_registerers_by_name,
            custom_op_registerers_by_func, experimental_preserve_all_tensors))
elif not model_content and not model_path:
    raise ValueError('`model_path` or `model_content` must be specified.')
else:
    raise ValueError('Can\'t both provide `model_path` and `model_content`')

if num_threads is not None:
    if not isinstance(num_threads, int):
        raise ValueError('type of num_threads should be int')
    if num_threads < 1:
        raise ValueError('num_threads should >= 1')
    self._interpreter.SetNumThreads(num_threads)

# Each delegate is a wrapper that owns the delegates that have been loaded
# as plugins. The interpreter wrapper will be using them, but we need to
# hold them in a list so that the lifetime is preserved at least as long as
# the interpreter wrapper.
self._delegates = []
if experimental_delegates:
    self._delegates = experimental_delegates
    for delegate in self._delegates:
        self._interpreter.ModifyGraphWithDelegate(
            delegate._get_native_delegate_pointer())  # pylint: disable=protected-access
self._signature_defs = self.get_signature_list()

self._metrics = metrics.TFLiteMetrics()
self._metrics.increase_counter_interpreter_creation()
