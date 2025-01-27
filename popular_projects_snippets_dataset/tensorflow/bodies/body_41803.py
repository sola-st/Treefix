# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
# Implements GenericFunction.__call__.
if self._run_functions_eagerly:
    with trace.Trace(self._name, tf_function_call="eager"):
        exit(self._python_function(*args, **kwds))

    # Only count the statistics the first time, before initialization took
    # place.
if self._created_variables is None:
    compiled = bool(self._jit_compile and
                    not control_flow_util.GraphOrParentsInXlaContext(
                        ops.get_default_graph()))
    # For nested functions, increment the counter only when a function with
    # jit_compile=True is called within a function with jit_compile=False. We
    # count this special case to correctly record that both jit_compile=True
    # and jit_compile=False is being used for parts of the outer function.
    if ops.executing_eagerly_outside_functions() and (
        context.executing_eagerly() or compiled):
        # Labels must be strings in Python, so we convert 'compiled' to a string
        _tf_function_counter.get_cell(str(int(compiled))).increase_by(1)

tracing_count = self.experimental_get_tracing_count()
with trace.Trace(self._name) as tm:
    # TODO(cheshire): Do not duplicate the XLAControlFlowContext annotation.
    compiler = "xla" if self._jit_compile else "nonXla"

    with OptionalXlaContext(self._jit_compile):
        result = self._call(*args, **kwds)

    new_tracing_count = self.experimental_get_tracing_count()
    without_tracing = (tracing_count == new_tracing_count)
    execution_mode = "notTraced" if without_tracing else "traced"
    tm.set_metadata(tf_function_call=execution_mode + "-" + compiler,
                    tracing_count=new_tracing_count)

if context.executing_eagerly():
    if without_tracing:
        _frequent_tracing_detector_manager.called_without_tracing(
            self._key_for_call_stats)
    else:
        _frequent_tracing_detector_manager.called_with_tracing(
            self._key_for_call_stats, self._python_function,
            self._omit_frequent_tracing_warning)

exit(result)
