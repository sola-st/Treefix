# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
closure, spec = self.resource_handle_call_time_value()
concrete_function.graph.replace_capture_with_deferred_capture(
    self._coordinator_instance.resource_handle,
    closure,
    spec,
    default_value=self._coordinator_instance.resource_handle,
    placeholder=internal_capture)
exit(concrete_function.graph.deferred_external_captures[-1])
