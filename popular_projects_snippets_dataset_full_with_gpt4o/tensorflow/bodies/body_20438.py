# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2.py
# For __init__, just capture the inference dense shape and call parent.
if 'tensor_core_shape' in kwargs:
    self._tensor_core_shape = kwargs['tensor_core_shape']
    del kwargs['tensor_core_shape']
if 'embedding_lookup_device' in kwargs:
    self._embedding_lookup_device = kwargs['embedding_lookup_device']
    del kwargs['embedding_lookup_device']
_TPUEmbeddingColumnV2.__init__(self, *args, **kwargs)
