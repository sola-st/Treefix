# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
if not callable(function):
    raise ValueError("Function passed to `ClusterCoordinator.schedule` must "
                     "be a callable object.")
self._args = args or ()
self._kwargs = kwargs or {}

_disallow_remote_value_as_input(self._args)
_disallow_remote_value_as_input(self._kwargs)

if isinstance(function, def_function.Function):
    replica_args = _select_worker_slice(0, self._args)
    replica_kwargs = _select_worker_slice(0, self._kwargs)

    # Note: no need to handle function registration failure since this kind of
    # failure will not raise exceptions as designed in the runtime. The
    # coordinator has to rely on subsequent operations that raise to catch
    # function registration failure.

    # Record the function tracing overhead. Note that we pass in the tracing
    # count of the def_function.Function as a state tracker, so that metrics
    # will only record the time for actual function tracing (i.e., excluding
    # function cache lookups).
    with metric_utils.monitored_timer(
        "function_tracing", state_tracker=function._get_tracing_count):  # pylint: disable=protected-access
        self._concrete_function = function.get_concrete_function(
            *nest.map_structure(_maybe_as_type_spec, replica_args),
            **nest.map_structure(_maybe_as_type_spec, replica_kwargs))
elif isinstance(function, tf_function.ConcreteFunction):
    self._concrete_function = function

if hasattr(self, "_concrete_function"):
    # If we have a concrete function, we get to retrieve the output type spec
    # via the structured_output.
    self._output_type_spec = func_graph.convert_structure_to_signature(
        self._concrete_function.structured_outputs)
    self._function = cancellation_mgr.get_cancelable_function(
        self._concrete_function)
else:
    # Otherwise (i.e. what is passed in is a regular python function), we have
    # no such information.
    self._output_type_spec = None
    self._function = function

self._output_remote_value_ref = None
