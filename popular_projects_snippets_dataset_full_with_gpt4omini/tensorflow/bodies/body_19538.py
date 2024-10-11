# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/profiler/profiler_analysis_pb2_grpc.py
"""Constructor.

    Args:
      channel: A grpc.Channel.
    """
self.NewSession = channel.unary_unary(
    '/tensorflow.ProfileAnalysis/NewSession',
    request_serializer=third__party_dot_tensorflow_dot_core_dot_profiler_dot_profiler__analysis__pb2
    .NewProfileSessionRequest.SerializeToString,
    response_deserializer=third__party_dot_tensorflow_dot_core_dot_profiler_dot_profiler__analysis__pb2
    .NewProfileSessionResponse.FromString,
)
self.EnumSessions = channel.unary_unary(
    '/tensorflow.ProfileAnalysis/EnumSessions',
    request_serializer=third__party_dot_tensorflow_dot_core_dot_profiler_dot_profiler__analysis__pb2
    .EnumProfileSessionsAndToolsRequest.SerializeToString,
    response_deserializer=third__party_dot_tensorflow_dot_core_dot_profiler_dot_profiler__analysis__pb2
    .EnumProfileSessionsAndToolsResponse.FromString,
)
self.GetSessionToolData = channel.unary_unary(
    '/tensorflow.ProfileAnalysis/GetSessionToolData',
    request_serializer=third__party_dot_tensorflow_dot_core_dot_profiler_dot_profiler__analysis__pb2
    .ProfileSessionDataRequest.SerializeToString,
    response_deserializer=third__party_dot_tensorflow_dot_core_dot_profiler_dot_profiler__analysis__pb2
    .ProfileSessionDataResponse.FromString,
)
