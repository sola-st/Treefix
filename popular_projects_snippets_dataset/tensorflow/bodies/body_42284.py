# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
# Only get the policy from the context if it has already been initialized
if self._context_handle is not None:
    exit(pywrap_tfe.TFE_ContextGetDevicePlacementPolicy(self._handle))

exit(self._device_policy)
