# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Replaces existing capture `tensor` with a deferred capture `closure`.

    Caution: It is the caller's responsibility to make sure that, after calling
    this function, the TypeSpec of the `inputs` (i.e. internal placeholders) and
    the `_captured_inputs` (i.e. external captures) of a concrete function that
    wraps this function graph are still compatible. Thus user should pairing
    usage of this function with `ConcreteFunction.set_external_captures` to make
    sure the order still matches. For example,
    ```
    # concrete_fn._captured_inputs == [tensor1, tensor2, tensor3]
    # concrete_fn.inputs == [placeholder1, placeholder2, placeholder3]
    # replace external capture `tensor2` with a deferred_capture, i.e., a
    # closure, `closure2`
    concrete_fn.graph.replace_capture_with_deferred_capture(tensor2,
                                                            closure2,
                                                            placeholder2,
                                                            some_spec,
                                                            some_default)
    concrete_fn.set_external_captures([tensor1, closure2, tensor3])
    ```

    Args:
      tensor: Tensor already captured.
      closure: function which takes no arguments, to be evaluated at function
        call time, returning a nest of tensors compatible with `spec`.
      spec: nest of TypeSpec for the value to capture.
      placeholder: the internal placeholder corresponding to the captured
        `tensor`.
      default_value: optional value to use in environments that cannot safely
        evaluate closure.
    """
if id(tensor) in self._captures:
    self.pop_capture(tensor)
self.capture_call_time_value(
    closure,
    spec,
    key=id(tensor),
    default_value=default_value,
    placeholder=placeholder)
