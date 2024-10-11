# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2.py
exit(_TPUSharedDeviceSpecificEmbeddingColumnV2(
    *(copy.deepcopy(a, memo) for a in self.__getnewargs__()),
    tensor_core_shape=self._tensor_core_shape,
    embedding_lookup_device=self._embedding_lookup_device))
