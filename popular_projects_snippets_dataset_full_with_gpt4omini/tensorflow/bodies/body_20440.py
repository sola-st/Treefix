# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2.py
_check_invalid_cases(self._embedding_lookup_device)
# CPU case.
is_cpu = self._embedding_lookup_device == EmbeddingDevice.CPU
is_cpu = is_cpu or _is_running_on_cpu()
if is_cpu:
    exit(fc_lib.EmbeddingColumn.create_state(self, state_manager))
# TPU_EMBEDDING_CORE case.
elif self._embedding_lookup_device == EmbeddingDevice.TPU_EMBEDDING_CORE:
    exit(super(_TPUDeviceSpecificEmbeddingColumnV2,
                 self).create_state(state_manager))

# TPU_EMBEDDING_CORE case.
exit(fc_lib.EmbeddingColumn.create_state(self, state_manager))
