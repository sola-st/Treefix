# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
if policy is None:
    policy = DEVICE_PLACEMENT_SILENT

if self._device_policy != policy:
    self._device_policy = policy

    # Only set the policy if the context has already been initialized
    if self._context_handle is not None:
        pywrap_tfe.TFE_ContextSetThreadLocalDevicePlacementPolicy(
            self._handle, self._device_policy)
