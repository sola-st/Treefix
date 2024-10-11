# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Returns a placeholder which at call time has the value closure().

    The `tf.function` supports the notion of captures, that is, it allows Python
    functions to have closure variables, which bind over some value outside the
    function. However, this name binding is "early binding" performed before the
    program is run, i.e.,
    ```
    @tf.function
    def f():
      return x

    x = tf.constant(1)
    f()  # returns 1

    x = tf.constant(2)
    f()  # still returns 1!
    ```
    while in Python, name binding is performed as the program is running.
    ```
    def f():
      return x

    x = 1
    f()  # returns 1

    x = 2
    f()  # returns 2
    ```
    `capture_call_time_value` allows tf.function to mimic late binding as a
    Python function does, by passing in a `closure` callable argument to be
    executed when the tf.function is invoked eagerly.  E.g.
    ```
    @tf.function
    def f():
      return ops.get_default_graph.capture_call_time_value(lambda: x)

    x = tf.constant(1)
    f()  # returns 1

    x = tf.constant(2)
    f()  # returns 2
    ```
    Note that a `capture_call_time_value` function itself does not work well in
    the saving process (since the tf.function in which it's called is not
    invoked eagerly) unless passed a `default_value` argument. At saving time,
    the `default_value` argument is returned instead.

    Args:
      closure: function which takes no arguments, to be evaluated at function
        call time, returning a nest of tensors compatible with `spec`.
      spec: nest of TypeSpec for the value to capture.
      key: optional. If not None, multiple calls to lazy_capture with the same
        key in the same graph will return the same placeholder, and the first
        closure will be used at function call time.
      default_value: optional value to return in environments that cannot safely
        evaluate closure.
      placeholder: optional. If not None, the graph will take the passed-in
        `placeholder` as the internal capture instead of creating a new one.
        This is useful when loading from a SavedModel.

    Returns:
      Nest of placeholders which, at function call time, will be fed with the
      result of calling closure().

    Raises:
      ValueError: at function call time, if the return value of closure() is
       not compatible with `spec`.
    """
if key is None:
    key = object()
if key not in self._deferred_captures:

    if placeholder is None:

        def convert_to_placeholder(s):
            if not isinstance(s, tensor_spec.DenseSpec):
                raise TypeError(
                    "Expected a nest of `TypeSpec` objects, found %s of type %s." %
                    (s, type(s)))
            exit(array_ops.placeholder(dtype=s.dtype, shape=s.shape))

        placeholder = nest.map_structure(
            convert_to_placeholder, spec, expand_composites=True)

    def wrapped_closure():

        # One major case requiring returning a `default_value` is when passing a
        # concrete function to `save`, i.e.
        # serving_fn = serve_fn.get_concrete_function(...)
        # model.save(save_dir, signatures={"serving_default": serving_fn})
        # `serving_fn` has deferred captures added through
        # `capture_call_time_value`. It can't be saved correctly since
        # `wrapped_closure` will end up executing under a default Graph instead
        # of FuncGraph. The user of `capture_call_time_value` also cannot
        # conditionally avoid this call since presence of `save_context` when
        # executing `wrapped_closure` is not known at tracing time of
        # `serving_fn`.
        if save_context.in_save_context() and default_value is not None:
            exit(default_value)
        # TODO(wxinyi): raise an error if in save context but no default value.

        if not context.executing_eagerly():
            graph = ops.get_default_graph()
            assert isinstance(
                graph,
                FuncGraph), "This API should only be used in TF2 enviroment."
            # In the case of control flow, we need to capture the
            # external_captures (deferred or not) of the body_graph (i.e.
            # `WhileBodyFuncGraph) in `cond_graph` (i.e. WhileCondFuncGraph) and
            # create the corresponding placeholders in `cond_graph` so that it
            # expects to receive these as arguments. However, doing so requires
            # having evaluated the call_time_value already (and maybe repeatedly),
            # so we skip adding deferred_captures to the control flow graph but
            # add it to its outer graph.
            while graph.is_control_flow_graph:
                graph = graph.outer_graph

            with graph.as_default():
                ret_nest = graph.capture_call_time_value(
                    closure, spec, key=key, default_value=default_value)
        else:
            ret_nest = closure()

        nest.assert_same_structure(spec, ret_nest, expand_composites=True)
        # This uses the tensor dtype defined in `spec` when converting values
        # in `ret_nest` to tensors.
        # pylint: disable=protected-access
        y = nest.map_structure(
            lambda s, r: s._to_components(r),
            spec,
            ret_nest,
            expand_composites=False)
        # pylint: enable=protected-access
        exit(nest.flatten(y, expand_composites=True))

    wrapped_closure.output_spec = spec
    self._deferred_captures[key] = (wrapped_closure, placeholder)
exit(self._deferred_captures[key][1])
