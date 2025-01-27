# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/profiler/profiler_analysis_pb2_grpc.py
rpc_method_handlers = {
    'NewSession':
        grpc.unary_unary_rpc_method_handler(
            servicer.NewSession,
            request_deserializer=third__party_dot_tensorflow_dot_core_dot_profiler_dot_profiler__analysis__pb2
            .NewProfileSessionRequest.FromString,
            response_serializer=third__party_dot_tensorflow_dot_core_dot_profiler_dot_profiler__analysis__pb2
            .NewProfileSessionResponse.SerializeToString,
        ),
    'EnumSessions':
        grpc.unary_unary_rpc_method_handler(
            servicer.EnumSessions,
            request_deserializer=third__party_dot_tensorflow_dot_core_dot_profiler_dot_profiler__analysis__pb2
            .EnumProfileSessionsAndToolsRequest.FromString,
            response_serializer=third__party_dot_tensorflow_dot_core_dot_profiler_dot_profiler__analysis__pb2
            .EnumProfileSessionsAndToolsResponse.SerializeToString,
        ),
    'GetSessionToolData':
        grpc.unary_unary_rpc_method_handler(
            servicer.GetSessionToolData,
            request_deserializer=third__party_dot_tensorflow_dot_core_dot_profiler_dot_profiler__analysis__pb2
            .ProfileSessionDataRequest.FromString,
            response_serializer=third__party_dot_tensorflow_dot_core_dot_profiler_dot_profiler__analysis__pb2
            .ProfileSessionDataResponse.SerializeToString,
        ),
}
generic_handler = grpc.method_handlers_generic_handler(
    'tensorflow.ProfileAnalysis', rpc_method_handlers)
server.add_generic_rpc_handlers((generic_handler,))
