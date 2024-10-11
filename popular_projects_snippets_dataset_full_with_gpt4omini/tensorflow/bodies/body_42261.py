# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Set virtual CPU devices in context.

    If virtual CPU devices are already configured at context initialization
    by tf.config.set_logical_device_configuration(), this method should not be
    called.

    Args:
      num_cpus: Number of virtual CPUs.
      prefix: Device name prefix.

    Raises:
     RuntimeError: If virtual CPUs are already configured at context
     initialization.
    """
server_def = self._server_def or self._collective_ops_server_def
local_prefix = ["/device"]
if server_def is not None:
    local_prefix.append("/job:%s/replica:0/task:%d" % (server_def.job_name,
                                                       server_def.task_index))
logical_local_devices = [d for d in self.list_logical_devices("CPU") if
                         d.name.startswith(tuple(local_prefix))]
self.ensure_initialized()
# Error out if there are already multiple logical CPU in the context.
if len(logical_local_devices) > 1:
    raise RuntimeError("Virtual CPUs already set, cannot modify again.")

pywrap_tfe.TFE_SetLogicalCpuDevices(self._context_handle, num_cpus, prefix)
self._initialize_logical_devices()
