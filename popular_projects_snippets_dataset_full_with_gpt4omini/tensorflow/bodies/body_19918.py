# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_hardware_feature.py
"""Convert the embedding feature proto to enum string."""
embedding_feature_proto_to_string_map = {
    topology_pb2.TPUHardwareFeature.EmbeddingFeature.UNSUPPORTED:
        HardwareFeature.EmbeddingFeature.UNSUPPORTED,
    topology_pb2.TPUHardwareFeature.EmbeddingFeature.V1:
        HardwareFeature.EmbeddingFeature.V1,
    topology_pb2.TPUHardwareFeature.EmbeddingFeature.V2:
        HardwareFeature.EmbeddingFeature.V2
}
exit(embedding_feature_proto_to_string_map.get(
    embedding_feature_proto, HardwareFeature.EmbeddingFeature.UNSUPPORTED))
