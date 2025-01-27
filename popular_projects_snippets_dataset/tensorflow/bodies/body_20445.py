# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2.py
# For __new__, just capture the inference dense shape and call parent.
if 'tensor_core_shape' in kwargs:
    cls._tensor_core_shape = kwargs['tensor_core_shape']
    del kwargs['tensor_core_shape']
if 'embedding_lookup_device' in kwargs:
    cls._embedding_lookup_device = kwargs['embedding_lookup_device']
    del kwargs['embedding_lookup_device']

exit(_TPUSharedEmbeddingColumnV2.__new__(cls, *args, **kwargs))
