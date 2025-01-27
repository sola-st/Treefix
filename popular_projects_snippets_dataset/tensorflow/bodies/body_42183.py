# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Helper to initialize devices."""
# Store list of devices
logical_devices = []
context_devices = []
device_list = pywrap_tfe.TFE_ContextListDevices(self._context_handle)
try:
    self._num_gpus = 0
    current_job, current_task = None, None
    server_def = self._server_def or self._collective_ops_server_def
    if server_def is not None:
        current_job, current_task = server_def.job_name, server_def.task_index
    for i in range(pywrap_tfe.TF_DeviceListCount(device_list)):
        dev_name = pywrap_tfe.TF_DeviceListName(device_list, i)
        context_devices.append(pydev.canonical_name(dev_name))
        spec = pydev.DeviceSpec.from_string(dev_name)
        # If the job is localhost, we assume that the cluster has not yet been
        # configured and thus clear the job, replica & task.
        if spec.job == "localhost":
            spec = spec.replace(job=None, replica=None, task=None)
        logical_devices.append(
            LogicalDevice(name=spec.to_string(), device_type=spec.device_type))
        dev_type = pywrap_tfe.TF_DeviceListType(device_list, i)
        if (dev_type == "GPU" and spec.job == current_job and
            spec.task == current_task):
            self._num_gpus += 1

finally:
    self._logical_devices = logical_devices
    self._context_devices = context_devices
    pywrap_tfe.TF_DeleteDeviceList(device_list)
