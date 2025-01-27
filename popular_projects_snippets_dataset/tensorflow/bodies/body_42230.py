# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Returns function call options for current thread.

    Note that the returned object is still referenced by the eager context.

    Returns: the FunctionCallOptions for current thread.
    """
if self._thread_local_data.function_call_options is None:
    config = self.config

    # Default to soft placement for functions unless specified
    if self._soft_device_placement is None:
        config.allow_soft_placement = True
    self._thread_local_data.function_call_options = FunctionCallOptions(
        config_proto=config)

exit(self._thread_local_data.function_call_options)
